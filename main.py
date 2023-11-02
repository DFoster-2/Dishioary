from PyDictionary import PyDictionary

word = input("enter a word: ")
dictionary = PyDictionary(word)

check = dictionary.getMeanings()

print(check)
input("press enter to exit")

go = "YES"
while go != "NO":
    print("-----------RESTART--------------RESTART----------------RESTART----------")

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ "
    stringtoencrypt = input ("please enter a message to encrypt:")
    stringtoencrypt = stringtoencrypt.upper()
    shiftamount = int(input("Please enter a whole number from 1-25 to be your key."))
    encrypyrdstring = ""
    for currentcharacter in stringtoencrypt:
        position = alphabet.find(currentcharacter)
        newposition = position + shiftamount
        if currentcharacter in alphabet:
            encrypyrdstring = encrypyrdstring + alphabet[newposition]
        else:
            encrypyrdstring = encrypyrdstring + alphabet[newposition]
        print(" your encrypted new message is", encrypyrdstring)
    print ("---------------------------------------------------------------------")
    print ()
    print(" Your message is", stringtoencrypt)
    print(" your encrypted message is", encrypyrdstring)  
    print ()
    print ("--------------------------------------------------------------------")
  
    go = input ("Press enter to to start again, or type No to leave").upper()
print(encrypyrdstring.isspace())