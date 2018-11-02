def crypt(a):
    length = len(a)
    encrypt = []
    for i in a:
        i = i.lower()
        encrypt.append(chr((ord(i)-97+1%26)+97))
    return "".join(encrypt);
