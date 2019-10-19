# Christian Piper
# 9/23/19
# Ths program will ask the user if anyone in the group is vegetarian/vegan/gluten free 
# and list the possible restaurants they could go to

def main():
    
    # Ask questions
    vegetarian = input("Is anyone in your party a vegetarian? (y/n) ")
    vegan = input("Is anyone in your party a vegan? (y/n) ")
    glutenFree = input("Is anyone in your party a gluten-free? (y/n) ")
    
    # Set variables to true/false values based on text input
    if vegetarian == 'yes' or vegetarian == 'y':
        vegetarian = True
    else:
        vegetarian = False
    
    if vegan == 'yes' or vegan == 'y':
        vegan = True
    else:
        vegan = False

    if glutenFree == 'yes' or glutenFree == 'y':
        glutenFree = True
    else:
        glutenFree = False
    
    #Print start line
    print("Here are your restaurant choices: ")

    # Create cases
    if vegetarian == True and vegan == True and glutenFree == True:
        case = "TTT"
    elif vegetarian == False and vegan == True and glutenFree == True:
        case = "FTT"
    elif vegetarian == True and vegan == False and glutenFree == True:
        case = "TFT"
    elif vegetarian == False and vegan == True and glutenFree == False:
        case = "FTF"
    elif vegetarian == True and vegan == True and glutenFree == False:
        case = "TTF"
    elif vegetarian == False and vegan == False and glutenFree == True:
        case = "FFT"
    elif vegetarian == True and vegan == False and glutenFree == False:
        case = "TFF"
    elif vegetarian == False and vegan == False and glutenFree == False:
        case = "FFF"
    
    #Print restaurants based on choices
    if case == "TTT":
        print("Jack's Greek Food Factory")
    elif case == "FTT":
        print("Jack's Greek Food Factory")
    elif case == "TFT":
        print("Sophie's Main Street Diner, Jack's Greek Food Factory, Isaac's Phenomenal Kitchen")
    elif case == "FTF":
        print("Hunter's Fancy Footwork Café, Jack's Greek Food Factory")
    elif case == "TTF":
        print("Hunter's Fancy Footwork Café, Jack's Greek Food Factory")
    elif case == "FFT":
        print("Sophie's Main Street Diner, Jack's Greek Food Factory, Isaac's Phenomenal Kitchen")
    elif case == "TFF":
        print("Sophie's Main Street Diner, Hunter's Fancy Footwork Café, Jack's Greek Food Factory, Isaac's Phenomenal Kitchen")
    elif case == "FFF":
        print("Christian's Gourmet's Burgers, Sophie's Main Street Diner, Hunter's Fancy Footwork Café, Jack's Greek Food Factory, Isaac's Phenomenal Kitchen")

main()