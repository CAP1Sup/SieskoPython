# Christian Piper
# 10/22/19
# This program is use to test various commands

def main():
    converted = ""

    message = input("Input your message: ")
    index = input("Input the index value: ")
    try:
        index = int(index)
        flag = False
    except:
        print("Make sure that the index is a valid integer")
        flag = True
    
    if flag == False:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        newAlph = alphabet[index:] + alphabet[:index]

    for i in range(len(message)):
        if not message[i] == " ":
            for j in range(len(alphabet)):
                if message[i] == alphabet[j]:
                    converted = converted + newAlph[j]
                    break
    
    print(converted)




main()