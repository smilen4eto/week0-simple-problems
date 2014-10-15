def sum_of_digits(n):
    n = str(abs(n))
    sum = 0
    for i in n:
        sum = sum + int(i)
    return sum

print(sum_of_digits(-46545))
