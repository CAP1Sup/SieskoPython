# Christian Piper
# 10/9/19
# This program will prompt the user for a number and print out all the even values less than that number

def main():
    # Run until user inputs a correct value
    while True:
        n = input("Input an integer: ")
        try:
            nInt = int(n)
            evenNum = nInt
            squareNum = nInt
            primeNum = nInt
            break
        except:
            continue

    print()
    print("Even numbers:")
    while evenNum >= 0:
        if evenNum % 2 == 0:
            print(evenNum)
            evenNum = evenNum - 2
        else:
            evenNum = evenNum - 1

    print()
    print("Perfect Squares:")
    while squareNum > 0:
        t = squareNum ** (1/2)
        if t.is_integer():
            print(squareNum)
        squareNum = squareNum - 1

    print()
    print("Prime #s:")
    for val in range(1, primeNum):
        if val > 1:
            for n in range(2, val):
                if (val % n ) == 0:
                    break
            else:
                print(val)
                continue    

main()
