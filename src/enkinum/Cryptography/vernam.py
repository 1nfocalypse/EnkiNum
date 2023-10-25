from random import randrange
import viginere
def vernam(cleartext):
    """
    Encrypts a string using a Vernam One-Time Pad generated pseudorandomly.
    This does not meet entropy standards. Use at your own risk.

    :param cleartext: string of data to encrypt
    :return: List of strings, ["key", "ciphertext"]
    """
    str_len = len(cleartext)
    key = ""
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    for i in range(str_len):
        key = key + chars[randrange(26)]

    return [key, viginere(cleartext, key)]

