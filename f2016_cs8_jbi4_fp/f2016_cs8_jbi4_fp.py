# Template for code submission
# name : Joseph Isaacson
# email : jbi4@pitt.edu
# date : 12/15/2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: Final Project
# Example:
#
# Notes: f2016_cs8_fp.data.txt

# Initialize a global dictionary
global_dict = {}
# Initialize the output file
outfile = open('f2016_cs8_jbi4_fp.data.output.csv', 'w')
outfile.write("Name, Records, Distance\n")


# Create the function process file
def processfile(fn, d):
    # open each file within the master file
    file = open(fn,'r')
    # read eachline of the file
    file.readline()
    # initialize the number of lines
    numlines = 0
    # read each line of the file
    for line in file:
        # strip the newline character and split the values
        line = line.rstrip('\n').split(",")
        # set the key and value in the line
        key, value = line
        # strip the right side of the key
        key = key.rstrip()
        # conditional if the key is already in the dictionary append it
        if key in d:
            d[key].append(float(value))
        # if the key is not in the dictionary add it to the dictionary
        else:
            d[key] = [float(value)]
        # counter for number of lines
        numlines += 1
    # close the file
    file.close()
    # return the new dictionary values and the total number of lines
    return d, numlines


# gain the name of the master list and open it
master = open(input("Name of file with all other file names: "), 'r')
# initialize the total number of lines
totalnumlines = 0
# initialize the number of files
numfiles = 0
# loop to read each file in the master file
for datafile in master:
    # remove the new line character
    datafile = datafile.rstrip('\n')
    # create a new list using the function
    mylist = processfile(datafile, global_dict)
    # update the dictionary with the first return value
    global_dict.update(mylist[0])
    # update the total lines with the partial lines from the function
    totalnumlines += mylist[1]
    # counter for the number of files
    numfiles += 1
# close the file
master.close()

# initialize the max distance
maxdist = 0
# initialize the max distance runner
maxname = " "
# initialize the min distance by setting the number higher so the min distance will go down
mindist = 10000000
# initialize the min distance runner
minname = " "
# initialize the number with multiple runs
nummulti = 0
# initialize the total distance
totaldist = 0

# loop for each item in the dictionary
for key in global_dict:
    # set llist to be equal to the key from the dictionary
    llist = global_dict[key]
    # conditional if the length of the key is greater than 1
    if len(llist) > 1:
        # if the key has multiple values count that the runner has more than one value
        nummulti += 1
    # set the partial dist to be equal to the sum of the values in llist
    pardist = sum(llist)
    # accumulate the partial distances to get the total distance
    totaldist += pardist
    # write the outfile by adding the key, the amount of times they ran and their distance run
    outfile.write(str(key) + ", " + str(len(llist))+ ", " + str(pardist) + '\n')
    # conditional if the current runner ran more than all the previous runners
    if max(llist) > maxdist:
        # set the new max distance
        maxdist = max(llist)
        # set the new key for who ran the most
        maxname = key
    # conditional if the current runner ran less than all the previous runners
    if min(llist) < mindist:
        # set the new min distance
        mindist = min(llist)
        # set the new key for who ran the least
        minname = key

outfile.close()

class Runinfo:
    name = "unknown"
    distance = 0
    runs = 0

    def __init__(self, name, dist=0):
        self.name = name
        if dist > 0:
            self.dist = dist
            self.runs = 1
    def addDistance(self, dist):
        if dist > 0:
            self.dist += dist
            self.runs += 1

    def addDistances(self, distances):
        for dist in distances:
            if dist > 0:
                self.dist += dist
                self.runs += 1
    def getName(self):
        return self.name
    def getDist(self):
        return self.dist
    def getRuns(self):
        return self.runs
    def __str__(self):
        return "Name :" + format(self.name, '>20s') + "Disance :" + format(self.dist, '9.4f') + "Runs :" \
        + format(self.runs, '4d')

    def tocsv(self):
        return ','.join((self.name, str(self.runs), str(self.dist)))



# print all of the outputs
print("Number of Input files read     : ", numfiles)
print("Total number of lines read     : ", totalnumlines)
print()
print("total distance run             : ", totaldist)
print()
print("max distance run               : ", maxdist)
print("   by participant              : ", maxname)
print()
print("min distance run               : ", mindist)
print("   by participant              : ", minname)
print()
print("Total number of participants   : ", len(global_dict))
print("Number of participants")
print("with multiple records          : ", nummulti)