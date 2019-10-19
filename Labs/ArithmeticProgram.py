# Christian Piper
# 9/3/19
# This program will prompt the user for two integers. The program will then print the sum, difference, product, quotient, and modulus to the screen. 
def main():
    # Program starts here
    
    # Get the first integer
    x1_str = input("Enter an integer:")
    x1 = int (x1_str)
    # Get the second integer
    x2_str = input("Enter the second integer:")
    x2 = int (x2_str)
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
    print("The sum is.........", sum)
    print("The difference is..", difference)
    print("The product is.....", product)
    print("The quotent is.....", quotent)
    print("The mod is.........", mod)

main()
