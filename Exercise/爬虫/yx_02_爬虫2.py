def sum_number(num):
    if num == 1:
        return 1

    temp = sum_number(num - 1)
    return num + temp


result = sum_number(1000)
print(result)
