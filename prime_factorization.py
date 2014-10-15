def prime_factorization(n):
    factorlist = []
    loop = 2
    while loop <= n:
        if n % loop == 0:
            n /= loop
            factorlist.append(loop)
        else:
            loop += 1
    return tuple((i, factorlist.count(i)) for i in factorlist)

print(prime_factorization(356))
