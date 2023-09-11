def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    shift %= 26
    for el in plaintext:
        if el.isalpha():
            letter = chr(ord(el) + shift)
            if not letter.isalpha():
                letter = chr(ord(el) + shift - 26)
            ciphertext += letter
        else:
            ciphertext += el
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    shift %= 26
    for el in ciphertext:
        if el.isalpha():
            letter = chr(ord(el) - shift)
            if not letter.isalpha():
                letter = chr(ord(el) - shift + 26)
            plaintext += letter
        else:
            plaintext += el
    return plaintext
