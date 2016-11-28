# Template for code submission
# name : Joseph Isaacson
# email : jbi4@pitt.edu
# date : 10/29/2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: Second Assignment
# Example:
#
# Notes:
# MN: respect indentation with comments too

# define the process file function
def processfile(fo):
    # initialize the variables for partial lines and partial distance
    pl = 0
    pd = 0
    # loop for each line in the file
    for line in fo:
        # remove the new line character and split the line, then make the second term a float
        line = line.rstrip('\n')
        temp = line.split(',')
        dist = float(temp[1])
        # use a counter for partial lines and an accumulator for the distance
        pd += dist
        pl += 1
    # return the numbers for partial distance and partial lines
    return pd, pl

# define the printkv function
def printkv(key, value, klen=0):
    # set an amount for howlong the key is
    kl = max(len(key), klen)
    # use if else if to determine what the value is and then set a format for each possible type
    if isinstance(value, str):
        fs = '20s'
    elif isinstance(value, float):
        fs = '10.3f'
    elif isinstance(value, int):
        fs = '10d'
    else:
        print("Error")
    print(format(key, str(kl)+'s'), format(value, fs))

# Code body
# initialize the variables for total lines and total distance
td = 0
tl = 0
# ask the user to input a file to process
file = input('First file: ')
# loop the file as long as there is a file name
while file and file != "q" and file != "quit":
    # open the file and run the process file function
    fo = open(file, 'r')
    pd, pl = processfile(fo)
    # run the printkv function to show the partial totals
    printkv("Partial Total # of lines   : ", pl)
    printkv("Partial distance run       : ", pd)
    # close the file
    fo.close()
    # run an accumulator to total the number of lines and total distance
    td += pd
    tl += pl
    # ask the user to input the next file to process
    file = input("Next file: ")

# print the total amounts for lines and distance
printkv("Total # of lines           : ", tl)
printkv("Total distance run         : ", td)











