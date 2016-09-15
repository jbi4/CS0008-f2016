# Template for code submission
# name : Joseph Isaacson
# email : jbi4@pitt.edu
# date : 9/6/2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description: Ask a user to give land area in square meters and convert the land area to acres and print
# Example: Starting with Python, Chapter 2, Exercise 3
#
# Notes:
# One acre of land is equivalent to 4,046.8564224 m2 (square meters).
# Write a program that asks the user to enter the total square meters of land and calculates the number of acres in the
# tract.

# Ask the user to enter in the total square meters of land
total_land_m2 = float(input("What is the total land in square meters? Please use only numbers:"))

# Conversion factor square meters to acres
meter_acres = 4046.8564224

# Convert square meters into acres
acres = total_land_m2/meter_acres

# Print amount of acres
print(acres)