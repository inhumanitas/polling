# coding=utf-8
import rsa
import base64


class RSAWrapper(object):
    u""" We can work with rsa"""
    PEM_MARKER_FORMAT = u"-----BEGIN RSA PUBLIC KEY-----\n%s\n-----END RSA PUBLIC KEY-----\n"

    def __init__(self):
        super(RSAWrapper, self).__init__()
        self._p_k = None
        self._pr_k = None
        self.rsa_gen_keys(1024)

    def get_public_key(self):
        u""" returns public key PEM """
        return self._p_k.save_pkcs1()

    def get_private_key(self):
        u""" returns private key PEM """
        return self._pr_k.save_pkcs1()

    def rsa_gen_keys(self, bits=1024):
        """
        @param: bits - Key length, in bits
        @return: Tuple of (secret, public) new RSA keys in PEM format
        """
        self._p_k, self._pr_k = rsa.newkeys(bits)

        return self.get_public_key(), self.get_private_key()

    def decrypt_str(self, encoded_str):
        str = base64.b64decode(encoded_str)
        decrypted_str = rsa.decrypt(str, self._pr_k)
        return decrypted_str