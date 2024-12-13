def main():
    print("Do you want to (e)ncrypt or (d)ecrypt ?")
    choice = input("> ")
    while choice!="e" and choice!="d":
        print("You must enter e or d !!")
        choice = input("> ")

    print("Please enter the key (0 to 25) to use .")
    key = int(input("> "))
    while not(0<=key<=25):
        print("The key must be between 0 and 25 !!")
        key = int(input("> "))
    
    if choice == "e":
        print("Enter the message to encrypt : ")
        text = input("> ")
        encrypt(text,key)
    else:
        print("Enter the message to decrypt : ")
        text = input("> ")
        decrypt(text,key)


def encrypt(text,key):
    crypt_text = ""
    for letter in text:
        if "A"<=letter.upper()<="Z":
            if ord(letter.upper())+key>90:
                crypt_text += chr(64+(ord(letter.upper())+key-90))
            else:
                crypt_text += chr(ord(letter.upper())+key)
        else:
            crypt_text += letter
    
    print(crypt_text+"\n"+"Full encrypted text")

def decrypt(text,key):
    crypt_text = ""
    for letter in text:
        if "A"<=letter.upper()<="Z":
            if ord(letter.upper())-key<65:
                crypt_text += chr(90-(64-(ord(letter.upper())-key)))
            else:
                crypt_text += chr(ord(letter.upper())-key)
        else:
            crypt_text += letter
    
    print(crypt_text+"\n"+"Full decrypted text")


main()