# Christian Piper
# 9/17/19
# This program will prompt the user for the amount of hours worked (in a week), and the hourly rate. 
# It will then calculate the pay of the week

def main():
    # Ask the user for the hours worked and the hourly rate
    hworked = input("Input the number of hours you worked this week: ")
    rate = input("Input your hourly rate: ")
    #Create pay variables
    pay = 0
    #Convert values
    hworked = float(hworked)
    rate = float(rate)
    pay = float(pay)
    #Read calculate pay
    if hworked <= 40:
        pay = hworked * rate
    else:
        pay = (hworked * rate) + ((hworked - 40) * (rate * .5))
    #Print results
    print("You will be paid: ", pay, "dollars")

main()
