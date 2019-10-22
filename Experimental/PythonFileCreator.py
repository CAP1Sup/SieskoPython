# Christian Piper
# 10/22/19
# This program will autogenerate a python template

from datetime import date

def main():
    name = input("Enter your name: ")
    # Needs to be fixed
    currentDate = date.today()
    purpose = input("Enter what the program will do: ")
    
    # Convert the stuff
    name = "# " + name + "\n"
    currentDate = "# " + currentDate + "\n"
    purpose = "# " + purpose + "\n"

    total = name + currentDate + purpose

    print(total)

main()