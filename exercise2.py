#Write a program to prompt for a file name, and then read
#through the file and look for lines of the form:
#When you encounter a line that starts with “X-DSPAM-Confidence:”
#pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence
#values from these lines. When you reach the end of the file, print out
#the average spam confidence.

#prompt user to enter file name
fname = input("Enter the file name: ")

fhand = open(fname)

n = 0
t = 0

for line in fhand:

    if not line.rstrip().startswith('X-DSPAM-Confidence:'): continue
    findNum = line.find('0')
    extract = float(line[findNum-1:])
    n+=1
    t+=extract

avg = t / n

print("Average spam confidence: ", avg )
