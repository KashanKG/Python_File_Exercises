#Exercise 3: Sometimes when programmers get bored or want to have a
#bit of fun, they add a harmless Easter Egg to their program. Modify
#the program that prompts the user for the file name so that it prints a
#funny message when the user types in the exact file name “na na boo
#boo”. The program should behave normally for all other files which
#exist and don’t exist.

fName = input("Enter the file name: ")

try:
    fhand = open(fName, 'r')

    inp = fhand.read()

    total_lines = len(inp)

    print("There were %d subject lines in %s" %(total_lines, fName))

except:
    print("File cannot be opened: ", fName)
