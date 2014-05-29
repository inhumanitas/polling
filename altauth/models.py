# coding=utf-8
import random
import rsa

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from altauth.utils import get_rsa_public_key_from_ssh_public_key

ALLOWED_PUBLICKEY_TYPES = (
    ('RSA', 'RSA'),
)

# This token length requires a minimum size of 64 for public keys
TOKEN_MIN_LENGTH, TOKEN_MAX_LENGTH = (30, 60)


class PollingUser(User):
    pasport_data = models.CharField(max_length=500)


def check_alt_key(user, alt_key):
    u""" Is user has the same key """
    return get_user_alt_key(user) == alt_key


def get_user_alt_key(user):
    try:
        alt_pass_obj = AlternativePassword.objects.get(
            user=user)
        alt_pass = alt_pass_obj.alternative_password
    except AlternativePassword.DoesNotExist:
        alt_pass = None
    return alt_pass


class AlternativePassword(models.Model):
    """
    Stores an alternative password for the user.
    This is useful for scripting, when users don't want to store
    their personal passwords in a script
    """
    user = models.OneToOneField(PollingUser)
    alternative_password = models.CharField(
        'alternative password', max_length=128)


class PublicKeyLoginToken(models.Model):
    """
    Saves a temporary login token to be used with public key authentication
    """
    public_key = models.OneToOneField('PublicKey')
    token = models.CharField('public key', max_length=TOKEN_MAX_LENGTH)

    @staticmethod
    def generate_token(length=None):
        """
            Generates a token to be used to log in
        """
        length = length or random.randint(TOKEN_MIN_LENGTH, TOKEN_MAX_LENGTH)
        return get_random_string(length)

    def check_token_is_valid(self, token):
        """
        Check if the token is valid (i.e. the user can log in)
        """
        return self.token == token


class PublicKey(models.Model):
    """
    Stores a public key for the user for pubkey authentication.

    """
    user = models.OneToOneField(PollingUser)
    public_key = models.CharField('public key', max_length=500)
    pubkey_type = models.CharField(
        'public key type', max_length=500, choices=ALLOWED_PUBLICKEY_TYPES)

    def get_server_key_for_pubkey_type(self, key_type=None, public=True):
        """
        returns the server public/private key
        for the corresponding key type
        ( not used in the current version )
        """
        key_type = key_type or self.pubkey_type
        if key_type == 'RSA':
            return settings.ALTAUTH_RSA_PUBLIC_KEY if public else (
                settings.ALTAUTH_RSA_PRIVATE_KEY)
        else:
            raise ValueError('pubkey type not supported: %s' % (key_type, ))

    def save(self, *args, **kwargs):
        """
        Overriding save method to cleanup in case of
        ssh public key
        """
        if self.pubkey_type == 'RSA':
            # We convert the public key in PEM format if it's
            # and RSA one.
            if self.public_key.startswith('ssh-rsa '):
                self.public_key = get_rsa_public_key_from_ssh_public_key(
                    self.public_key).save_pkcs1()
        super(PublicKey, self).save(*args, **kwargs)

    def generate_login_token(self):
        """
        generates a PublicKeyLoginToken instance and returns the login
        token encrypted
        """
        #server_public_key = self.get_server_key_for_pubkey_type(self.pubkey_type)
        token = PublicKeyLoginToken.generate_token()
        #message = "{} {} {}".format(len(token),token,server_public_key)
        message = token
        if self.pubkey_type == 'RSA':
            public_key = rsa.PublicKey.load_pkcs1(self.public_key)
            crypto_message = rsa.encrypt(str(message), public_key)
        else:
            raise ValueError(
                'pubkey type not supported: %s' % (self.public_key, ))

        public_key_login_token, created = (
            PublicKeyLoginToken.objects.get_or_create(public_key = self))
        public_key_login_token.token = token
        public_key_login_token.save()
        return crypto_message
