def last(n):
    num = n
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        print(num)
        num = num // 10
    return num