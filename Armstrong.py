def armstrong(num):
    n = len(str(num))
    sum = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    return True if sum == num else False

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = int(input())
    print(armstrong(number))
    print(prime(number))
    
    

# number = 153

# digit = 153 % 10 = 3
# sum = 0 + 3**3 = 27
# temp = 153 // 10 = 15

# digit = 15 % 10 = 5
# sum = 27 + 5**3 = 27 + 125 = 152
# temp = 15 // 10 = 1

# digit = 1 % 10 = 1
# sum = 152 + 1**3 = 152 + 1 = 153
# temp = 1 // 10 = 0

# 153 == 153 -> True