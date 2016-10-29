# Template for code submission
# name : Joseph Isaacson
# email : jbi4@pitt.edu
# date : 10/29/2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: Second Assignment
# Example: Assignment 12
#
# Notes:

# define the process file function
def processfile(fo):
    pl = 0
    pd = 0
    for line in fo:
        line = line.rstrip('\n')
        temp = line.split(',')
        dist = float(temp[1])
        pd += dist
        pl += 1
        return pd, pl

# define the printkv function
def printkv(key, value, klen=0):
    kl = max(len(key), klen)
    if isinstance(value, str):
        fs = '20s'
    elif isinstance(value, float):
        fs = '10.3f'
    elif isinstance(value, int):
        fs = '10d'
    print(format(key, str(kl)+'s'), format(value, fs))

# Code body
td = 0
tl = 0
file = input('First file: ')
while file and file != "q" and file != "quit":
    fo = open(file, 'r')
    pd, pl = processfile(fo)
    printkv("Partial Total # of lines: ", pl)
    printkv("Partial distance run: ", pd)
    fo.close()
    td += pd
    tl += pl
    file = input("Next file: ")

printkv("Total # of lines: ", tl)
printkv("Total distance run: ", td)











