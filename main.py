# Print last digits in a number
def last(n):
    num = n
    while num > 0:
        last_digit = num % 10
        print(last_digit)
        print(num)
        num = num // 10
    return num

# Count the number of digits in a number # time complexity is O(log10(n))
def count(n):
    num = n
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

# Check if a number is palindrome # time complexity is O(log10(n))
def palindrome(n):
    num = n
    result = 0
    while num > 0:
        last_digit = num % 10
        result = result * 10 + last_digit
        num = num // 10
        print(result)
    return "It is a palindrome" if n == result else "Not a palindrome"
     
# check if a string is palindrome
def stringpalindrome(s):
    string = s
    if string == string[::-1]:
        print(string)
        return "It is a palindrome"
    else:
        return "Not a palindrome"
    
# Check if the number is a armstrong number # Time complexity is O(log10(n))
def armstrong(n):
    num = n
    total = 0
    nod = len(str(n))
    while num > 0:
        digit = num % 10
        total = total + (digit ** nod)
        num = num // 10
    return "It is a armstrong number" if n == total else "Not an armstrong number"

# Print all factors of a number # This is a brute force approach 
# Time Complexity is O(n)
def factors(n):
    num = n
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return "The factors are " + str(result)

# optimal approach to print all factors of a number
# Time complexity is O(n/2)
def factors_optimal(n):
    num = n
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return "The factors are" + str(result)

# another optimal approach to print all factors of a number
# Time complexitys is O(sqrt(n)), O(nlogn)
from math import sqrt
def factors_optimal_2(n):
    num = n
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if num // i != i:
                result.append(num//i)
        result.sort()
    return "The factors are" + str(result)

if __name__ == "__main__":
    # arr = list(map(int, input().split()))
    n = int(input())
    # print(last(n))
    # print(count(n))
    # print(palindrome(n))
    # s = input()
    # print(stringpalindrome(s))
    # print(armstrong(n))
    # print(factors(n))
    # print(factors_optimal(n))
    print(factors_optimal_2(n))
