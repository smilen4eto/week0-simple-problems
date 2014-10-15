def prime_number_of_divisors(n):
    div = [i for i in range(1, n) if n % i == 0]
    p = len(div) + 1
    l = p
    if p == 2:
        return True
    else:
        for i in range(2, p):
            if l % i == 0:
                return False
            else:
                return True

print(prime_number_of_divisors(8))
