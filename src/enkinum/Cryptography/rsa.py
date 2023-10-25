def rsa(p, q, e, cbool, d=0):
    """
    Toy RSA implementation w/o padding.

    :param p: large prime
    :param q: large prime
    :param e: encryption exponent coprime with phi ((p-1)(q-1))
    :param cbool: 0 for encryption, 1 for decryption

    :return: Array of strings [public, private, cipher/cleartext]
    """
