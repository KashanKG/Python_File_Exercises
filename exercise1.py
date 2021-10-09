#Exercise 1: Write a program to read through a file and print the contents
#of the file (line by line) all in upper case.

fh = open("mbox-short.txt")
print(fh)

for line in fh:
    upperLine = line.rstrip().upper()
    print(upperLine)
