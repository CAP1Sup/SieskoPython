# Christian Piper
# 9/9/19
# This program will ask the user for a few words and then create a story like a Mad Libs paper.
def main():
    name = input("Please put in the name of a person: ")
    verb1 = input("Please input a verb in infinitive form: ")
    noun = input("Please input a proper noun: ")
    ability = input("Please input an ability in infinitive form (ex fly): ")
    num1 = input("Please input a number: ")
    unit1 = input("Please input a unit that has to do with the ability: ")
    ability2 = input("Please enter a second ability: ")
    num2 = input("Please input a second number: ")
    unit2 = input("Please input a second unit (in infinitive) that would fit with the second ability: ")
    deathDate = input("Please input a date in the future: ")

    print()    
    print("One day,", name, "was", verb1, "in a forest.")
    print("All of the sudden,", name, "fell asleep.")
    nameWithS = (name + "'s")
    print("Then,", noun, "appeared in", nameWithS, "dream")
    print(name, "woke up suddenly.")
    print(name, "went home, and felt tired, so", name, "went to bed.")
    print("The next morning,", name, "had the ability to", ability)
    print(name, "discovered that he/she could", ability, "at", num1, unit1)
    print(name, "also found at that he/she could", ability2, "at", num2, unit2)
    print(name, "saved the world from the plans of the evil Doctor Siesko. He then promptly enjoyed the rest of his life until the day he died,", deathDate)

main()
