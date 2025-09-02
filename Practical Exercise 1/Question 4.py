#Here the user will be asked to enter a cetain character
#and the program will check to see whether that character 
#is in Uppercase or Lowercase.

#I went ahead to also include if that character is a digit
#or else a special character
character =int(input("Enter a Character"))
if character >="A" and character <="Z":
    print(character, "Is an Uppercase Letter")
elif character>="a" and character <="z":
    print(character, "Is a Lowercase Letter")
elif character>="0" and character <="9":
   print(character, "Is a Digit")
else: print(character, "Is a Special Symbol")   