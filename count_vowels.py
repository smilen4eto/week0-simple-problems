def count_vowels(str):
    str = str.lower()
    c = 0
    for i in str:
        if i in "aeiouy":
            c += 1
        return c

print(count_vowels("Hello, World!!"))
