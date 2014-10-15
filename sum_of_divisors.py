def sum_of_divisors(n):
    div = [i for i in range(1, n) if n % i == 0]
    sumd = 0
    for f in range(0, len(div)):
        sumd = sumd + div[f]
    return sumd + n

print (sum_of_divisors(8))
