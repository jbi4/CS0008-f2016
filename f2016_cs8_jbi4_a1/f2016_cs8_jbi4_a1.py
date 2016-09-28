# Template for code submission
# name : Joseph Isaacson
# email : jbi4@pitt.edu
# date : 9/30/2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: First assignment to help a client be able to better understand gas mileage
# Example: Assignment 1 Exercise 16 on the test
#
# Notes:


#Start by asking what unit of measure the user would like to enter the data as
uom = input("What unit of measure would you like to use, USC or Metric?")
#Have the user input the distance driven and gas used in metrics and convert to USC
if uom == "Metric" or uom == "metric":
    ddm = float(input("Distance driven in Km?"))
    gum = float(input("Gas used in Liters?"))
    ddu = ddm * .621371
    guu = gum * .264172
#Have the user input the distance driven and gas used in USC and convert to metric
elif uom == "USC" or uom == "usc":
    ddu = float(input("Distance driven in miles?"))
    guu = float(input("Gas used in gallons?"))
    ddm = ddu * 1.60934
    gum = guu * 3.78541
#print error if an invalic unit of measure was given
else:
    print("Error: Invalid unit of measure.")
