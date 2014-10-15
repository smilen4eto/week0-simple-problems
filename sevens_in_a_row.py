def sevens_in_a_row(arr, n):
    for i in range(len(arr) - n):
        if arr[i] == 7:
            result = True
            for k in range(i+1, i+n):
                if arr[k] != 7:
                    result = False
            if result:
                break
    return result

print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 7, 20, -7], 3))
