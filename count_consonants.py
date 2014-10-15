def count_consonants(str):
    str = str.lower()
    c = 0
    for i in str:
        if i in "bcdfghjklmnpqrstvwxz":
            c += 1
    return c

print(count_consonants("Grrrrgh!"))
