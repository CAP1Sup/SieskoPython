# Christian Piper
# 10/22/19
# This program will do the following:
# a. The sum of all even numbers between 2 and 100 (inclusive).
# b. The sum of all squares between 1 and 100 (inclusive).
# c. The sum of all odd numbers between a and b (inclusive) where a and b are entered by the user and a < b. 
# d. The sum of all odd digits of n where n is entered by the user.. (For example, if n is 32677, the sum would be 3 + 7 + 7 = 17.)

def main():
    print("Sum of all evens from 2 to 100: " + str(sumOfAllEvenNums(start = 2, end = 100)))
    print("Sum of all perfect squares from 1 to 100: " + str(sumOfAllSquares(start = 1, end = 100)))
    while True:
        a = input("Input the start of the range of numbers for sum of the odd numbers: ")
        b = input("Input the end of the range of numbers for sum of the odd numbers: ")
        try:
            a = int(a)
            b = int(b)
            break
        except:
            print("Enter a valid integer for the start and end")
            continue
        if a >= b:
            print("Input a valid range")
            break
    print("The sum of the odd values in the range was: " + str(sumOfAllOddNums(start = a, end = b)))
    while True:
        n = input("Input number you'd like to sample the odd digits from: ")
        try:
            n = int(n)
            break
        except:
            print("Enter a valid number")
            continue
    print("The sum of the odd digits in the number was: " + str(sumOfOddDigits(num = n)))

        


def sumOfAllEvenNums(start, end):
    val = end
    sum = 0
    while val >= start:
        if (val % 2) == 0:
            sum = sum + val
        val = val - 1
    return sum

def sumOfAllSquares(start, end):
    val = end
    sum = 0
    while val >= start:
        t = val ** (1/2)
        if t.is_integer():
            sum = sum + t
        val = val - 1
    return round(sum, 0)

def sumOfAllOddNums(start, end):
    val = end
    sum = 0
    while val >= start:
        if (val % 2) == 1:
            sum = sum + val
        val = val - 1
    return sum

def sumOfOddDigits(num):
    digits = extractDigits(baseNum = num)
    sum = 0
    for val in digits:
        if (val % 2) == 1:
            sum = sum + val
    return sum

def extractDigits(baseNum):
    digits = [int(x) for x in str(baseNum)]
    return digits

main()