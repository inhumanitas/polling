# coding=utf-8
import rsa
import base64
from polling.settings import (
ALTAUTH_RSA_PRIVATE_KEY, ALTAUTH_RSA_PUBLIC_KEY)


class RSAWrapper(object):
    u""" We can work with rsa"""

    def __init__(self):
        super(RSAWrapper, self).__init__()
        self._p_k = ALTAUTH_RSA_PUBLIC_KEY
        self._pr_k = ALTAUTH_RSA_PRIVATE_KEY
        self.rsa_gen_keys(1024)

    def get_public_key(self):
        u""" returns public key PEM """
        #return self._p_k.save_pkcs1().replace('RSA ', '')
        return self._p_k

    def get_private_key(self):
        u""" returns private key PEM """
        return self._pr_k

    def rsa_gen_keys(self, bits=1024):
        """
        @param: bits - Key length, in bits
        @return: Tuple of (secret, public) new RSA keys in PEM format
        """
        self.p_k, self.pr_k = rsa.newkeys(bits)

        return self.get_public_key(), self.get_private_key()

    def decrypt_str(self, encoded_str):
        str = base64.b64decode(encoded_str)
        pr_k = self.pr_k.load_pkcs1(self._pr_k)
        decrypted_str = rsa.decrypt(str, pr_k)
        return decrypted_str
