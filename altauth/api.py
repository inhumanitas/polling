# coding=utf-8
def rsa_gen_keys(bits=1024):
    """
    @param: bits - Key length, in bits
    @return: Tuple of (secret, public) new RSA keys in PEM format
    """
    import rsa

    return rsa.newkeys(bits)

PEM_MARKER_FORMAT = u"-----BEGIN RSA PUBLIC KEY-----\n%s\n-----END RSA PUBLIC KEY-----\n"