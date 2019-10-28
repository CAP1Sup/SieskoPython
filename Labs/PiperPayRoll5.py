# Christian Piper
# 10/28/19
# This program will calculate hourly wages and the commissions of workers and add them together at the end



def main():
    totalGrossPay = 0
    totalNetPay = 0
    totalFICA = 0
    totalStateTax = 0
    
    while True:
        # Get hourly or commission
        type = input("Enter H for hourly, C for commission: ")

        # Run hourly stuff if the worked is hourly
        if type == 'H' or type == 'h': 

            # Get worker's info
            hoursWorked = input("Input the hours worked: ")
            rate = input("Input the hourly rate: ")

            # Try to convert and restart if #s are invalid
            try:
                hoursWorked = float(hoursWorked)
            except:
                print("Input a valid number into hours worked")
                continue
            try:
                rate = float(rate)
            except:
                print("Input a valid number into rate")
                continue

            # Tell user to correct numbers if numbers are less than 0
            if hoursWorked < 0:
                print("Input a positive number into hours worked")
                continue
            if rate < 0:
                print("Input a positive number into rate")
                continue
            

            # Start printing
            print("")
            print("Initech Payroll Report")
            print("Hours worked:...............", hoursWorked)
            print("Hourly rate:................", rate)
            base = rate * hoursWorked
            overtime = .5 * (rate * (hoursWorked - 40))

            # Define gross variable
            gross = 0

            # If overtime
            if hoursWorked > 40:
                gross = base + overtime
                print("Gross:......................", round(gross, 2))
                print("Overtime:...................", round(overtime, 2))
            else:
                gross = base
                print("Gross:......................", round(base, 2))

        # Commission calculations
        elif type == 'C' or type == 'c':
            # Run commission code 
            totalSales = input("Input the total sales: ")
            base = 400
            bonus = 500

            # Convert text to an integer
            try:
                totalSales = float(totalSales)
            except:
                print("Input a valid number into hours worked")
                continue
            
            # Define the variables and do calculations
            gross = 0
            firstTierCommission = 0
            firstTier = (totalSales * 0.0525)
            saturatedFirstTier = 262.5
            secondTier = ((totalSales - 5000) * 0.035)

            # Calculate pay
            if totalSales <= 5000:
                gross = base + firstTier
                firstTierCommission = firstTier
                bonus = 0
            elif totalSales <= 25000:
                gross = base + saturatedFirstTier + secondTier
                firstTierCommission = saturatedFirstTier
                bonus = 0
            else:
                gross = base + saturatedFirstTier + secondTier + bonus
                firstTierCommission = saturatedFirstTier
                bonus = 500

            # Print calculations
            print("")
            print("Initech Payroll Report")
            print("Gross:......................", round(gross,2))
            print("First stage commission:.....", round(firstTierCommission, 2))
            if secondTier >= 0:
                print("Second tier commission:.....", round(secondTier, 2))
            print("Bonus:......................", bonus)


        else: 
            print("Input a valid character")
            continue

        # Do calculations
        fica = gross * 0.062
        stateTax = gross * 0.0307
        netPay = gross - fica - stateTax

        # Print calculations
        print("Fica:.......................", round(fica, 2))
        print("State:......................", round(stateTax, 2))
        print("Net Pay:....................", round(netPay, 2))

        # Total the values
        totalGrossPay = totalGrossPay + gross
        totalFICA = totalFICA + fica
        totalStateTax = totalStateTax + stateTax
        totalNetPay = totalNetPay + netPay
        
        # Ask if the user wants more calculations done
        more = input("Would you like to do more calculations? (y/n): ")
        if more == 'y' or more == 'No' or more == 'yes' or more == 'Yes':
            continue
        else:
            print("Thank you for using the Piper Industries Pay Calculator!")
            print("Total Gross......... " + str(totalGrossPay))
            print("Total FICA.......... " + str(totalFICA))
            print("Total State Tax..... " + str(totalStateTax))
            print("Total Net Pay....... " + str(totalNetPay))
            break
main()
