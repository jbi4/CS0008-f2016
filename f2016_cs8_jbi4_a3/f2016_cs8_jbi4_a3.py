# Template for code submission
# name : Joseph Isaacson
# email : jbi4@pitt.edu
# date : 11/18/2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: Third Assignment
# Example:
#
# Notes: f2016_cs8_a3.data.txt

# ask the user to input the master data file
fn = input("Name of file with all other file names: ")
# open the master data file
fh = open(fn, 'r')
# read all of the lines in the file
source = fh.readlines()
# make each file name separate without the new line character
source = [line.strip('\n') for line in source]
# close the master file
fh.close()

# initialize a new list
newlist = []
# open each individual file
for file in source:
    # open the file
    fh = open(file, 'r')
    # read all of the lines in the file
    datafile = fh.readlines()
    # make each list separate without the new line character
    datafile = [line.strip('\n').split(',') for line in datafile]
    datafile1 = datafile[1:]
    newlist.append(datafile1)
    str(newlist)
print(newlist)
print(len(newlist))