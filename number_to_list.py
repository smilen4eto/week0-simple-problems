def number_to_list(n):
    n = str(n)
    ln = []
    for i in range(0, len(n)):
        ln.append(n[i])
    return ln

print(number_to_list(65565))
