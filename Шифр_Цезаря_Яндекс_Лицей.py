# в шифр Цезаря
def encrypt_caesar(msg, shift=3):
    shift = shift % 32
    A = [i for i in msg]
    for i in range(len(A)):
        if A[i].isupper():
            if ord(msg[i]) + shift > 1071:
                A[i] = chr(1039 + ord(msg[i]) + shift - 1071)
            else:
                A[i] = chr(ord(msg[i]) + shift)
        elif A[i].islower():
            if ord(msg[i]) + shift > 1103:
                A[i] = chr(1071 + ord(msg[i]) + shift - 1103)
            else:
                A[i] = chr(ord(msg[i]) + shift)
    return ''.join(A)


# перевод из шифра Цезаря
def decrypt_caesar(msg, shift=3):
    shift = shift % 32
    A = [i for i in msg]
    for i in range(len(A)):
        if A[i].isupper():
            if ord(msg[i]) - shift < 1040:
                A[i] = chr(1072 - (1040 - (ord(msg[i]) - shift)))
            else:
                A[i] = chr(ord(msg[i]) - shift)
        elif A[i].islower():
            if ord(msg[i]) - shift < 1072:
                A[i] = chr(1104 - (1072 - (ord(msg[i]) - shift)))
            else:
                A[i] = chr(ord(msg[i]) - shift)
    return ''.join(A)

