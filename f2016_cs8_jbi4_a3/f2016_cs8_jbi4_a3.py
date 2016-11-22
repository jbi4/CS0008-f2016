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

# initialize a new list and a counter of files
newlist = []
numfiles = 0
# open each individual file
for file in source:
    # open the file
    fh = open(file, 'r')
    # read all of the lines in the file
    datafile = fh.readlines()
    # make each list separate without the new line character
    datafile = [line.strip('\n').split(',') for line in datafile]
    # remove the first line of each file, the line with name and distance
    datafile1 = datafile[1:]
    # append the new list so all of the entries are in 1 list
    newlist.append(datafile1)
    # count the number of files
    numfiles += 1

# flatten the list so there are 450 separate entries
flatlist = []
for sublist in newlist:
    for val in sublist:
        flatlist.append(val)
# flatten the list so there are 900 separate entries
flatlist2 = []
for sublist in flatlist:
    for val in sublist:
        flatlist2.append(val)




# initialize a variable for total distance
totaldist = 0
distlist = []
# calculate the total distance
for i in range(1, len(flatlist2), 2):
    totaldist += float(flatlist2[i])
    distlist.append(float(flatlist2[i]))
    # get the max and min distance
    maxdist = max(distlist)
    mindist = min(distlist)

maxname = 0
minname = 0



print("Number of Input files read     : ", numfiles)
print("Total number of lines read     : ", len(flatlist))
print()
print("total distance run             : ", totaldist)
print()
print("max distance run               : ", maxdist)
print("   by participant              : ", maxname)
print()
print("min distance run               : ", mindist)
print("   by participant              : ", minname)
print()
print("Total number of participants   : ", )
print("Number of participants")
print("with multiple records          : ", )

