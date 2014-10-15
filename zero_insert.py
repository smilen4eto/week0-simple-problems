def zero_insert(n):
    n = str(n)
    d = len(n) - 1
    while d > 0:
        if (n[d] == n[d-1]) or (int(n[d])+int(n[d-1])) % 10 == 0:
            n = n[:d] + '0' + n[d:]
        d = d - 1
    return n

print(zero_insert(55555555))
