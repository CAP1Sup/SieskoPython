# Christian Piper
# 11/1/19
# This program will have the functions for add, subtract, multiply, divide, and modulus

def main():
    z = input("Enter the first value: ")
    x = input("Enter the second value: ")

    namings = ["sum", "difference", "product", "quotent", "modulus"]
    results = [add(z,x), subtract(z,x), multiply(z,x), divide(z,x), modulus(z,x)]
    
    for entry in range(0,5):
        print("The " + namings[entry] + " was " + str(results[entry]))
    

def convertToInt(x):
    try:
        x = int(x)
    except:
        print("Issue converting!")
    return x

def add(z, x):
    result = convertToInt(z) + convertToInt(x)
    return result

def subtract(z, x):
    result = convertToInt(z) - convertToInt(x)
    return result

def multiply(z, x):
    result = convertToInt(z) * convertToInt(x)
    return result

def divide(z, x):
    if not x == 0:
        result = convertToInt(z) / convertToInt(x)
    
    else:
        result = "Can't divide by 0!"

    return result

def modulus(z, x):
    result = convertToInt(z) % convertToInt(x)
    return result

main()