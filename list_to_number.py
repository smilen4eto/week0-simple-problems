def list_to_number(digits):
    i = 1
    n = len(digits)
    st = 10**(n-1)
    c = 0

    for i in range(0, n):
        c = c + digits[i]*st
        st = st/10
    return int(c)

print(list_to_number([9, 9, 9, 9, 9]))
