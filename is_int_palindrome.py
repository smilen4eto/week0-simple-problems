def is_int_palindrome(n):
    n = str(n)
    pal = []
    for i in range(0, len(n)):
        pal.append(n[i])
    pal2 = pal[::-1]

    if pal == pal2:
        return True
    else:
        return False

print(is_int_palindrome(88))
