def count_substrings(haystack, needle):
    if needle in haystack:
        haystack.split().index(needle)
        return haystack.count(needle)
    else:
        return 0

print(count_substrings("This is this and that is this", "this"))
