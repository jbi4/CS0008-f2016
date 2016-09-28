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
#Have the user input the distance driven and gas used in metrics, check to make sure inputs are positive, and convert to USC
if uom == "Metric" or uom == "metric":
    ddm = float(input("Distance driven in Km?"))
    gum = float(input("Gas used in Liters?"))
    if ddm < 0 or gum < 0:
        print("Error: Invalid inputs.")
    ddu = ddm * .621371
    guu = gum * .264172
#Have the user input the distance driven and gas used in USC, check to make sure inputs are positive, and convert to metric
elif uom == "USC" or uom == "usc":
    ddu = float(input("Distance driven in miles?"))
    guu = float(input("Gas used in gallons?"))
    if ddu < 0 or guu < 0:
        print("Error: Invalid inputs.")
    ddm = ddu * 1.60934
    gum = guu * 3.78541
#print error if an invalic unit of measure was given
else:
    print("Error: Invalid unit of measure.")
#calculate the fuel consumption in metric and usc
fcm = 100 * gum / ddm
fcu = ddu / guu
#use the fuel consumption in metrics to calculate the gas consumption rating
if fcm > 20:
    gcr = "Extremely poor"
elif fcm > 15 and fcm <= 20:
    gcr = "Poor"
elif fcm > 10 and fcm <= 15:
    gcr = "Average"
elif fcm > 8 and fcm <= 10:
    gcr = "Good"
else:
    gcr = "Excellent"