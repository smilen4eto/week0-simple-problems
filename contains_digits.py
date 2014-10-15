def contains_digits(number, digits):
    dig = str(number)
    for i in digits:
        if not(str(i) in dig):
            return False
    else:
        return True

print(contains_digits(123456789, [6, 5]))
