def contains_digit(number, digit):
    dig = str(number)
    if str(digit) in dig:
        return True
    else:
        return False

print(contains_digit(4548, 2))
