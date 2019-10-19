# Christian Piper
# 9/3/19
# This program will prompt the user for two integers. The program will then print the sum, difference, product, quotient, and modulus to the screen. 
def main():
    # Program starts here
    
    # Get the first integer
    x1Str = input("Enter an integer:")
    # Convert the raw input to an integer
    x1 = int (x1Str)
    # Get the second integer
    x2Str = input("Enter the second integer:")
    # Convert the raw input to an integer
    x2 = int (x2Str)
    # Compute sum
    sum = x1 + x2
    # Compute difference
    difference = x1 - x2
    # Compute product
    product = x1 * x2
    # Compute quotent
    quotent = x1 / x2
    # Compute mod
    mod = x1 % x2

    # Print everything
    print("The sum is.........", x1, "+", x2, '=', sum)
    print("The difference is..", x1, "-", x2, '=',difference)
    print("The product is.....", x1, "*", x2, '=',product)
    print("The quotent is.....", x1, "/", x2, '=',quotent)
    print("The mod is.........", x1, "%", x2, '=',mod)

main()
