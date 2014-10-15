def is_number_balanced(n):
    n = str(n)
    l = len(n)
    pal = []
    len1 = 0
    len2 = 0
    for i in range(0, len(n)):
        pal.append(n[i])
    pal2 = pal[::-1]

    for i in range(0, int(l/2)):
        len1 = len1 + int(pal[i])
        len2 = len2 + int(pal2[i])
    if len1 == len2:
        return True
    else:
        return False

print(is_number_balanced(28471))
