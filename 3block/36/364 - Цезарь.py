def encrypt_caesar(msg, shift=3):
    res = ''
    for letter in msg:

        if 1040 <= ord(letter) <= 1071:
            res += chr(ord(letter)+shift) if 1040 <= ord(letter)+shift <= 1071 else chr(ord(letter)+shift-32)
        elif 1072 <= ord(letter) <= 1103:
            res += chr(ord(letter)+shift) if 1072 <= ord(letter)+shift <= 1103 else chr(ord(letter)+shift-32)
        else:
            res += letter

    return res


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, 32-shift)


def main():
    msg = "Да здравствует салат Цезарь!"
    shift = 3
    encrypted = encrypt_caesar(msg, shift)
    decrypted = decrypt_caesar(encrypted, shift)
    print(encrypted)
    print(decrypted)


main()
