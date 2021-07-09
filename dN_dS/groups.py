#!/bin/python
#this script will write files that have orthogroups whose dN/dS ratios follow a specific pattern
    #ie high = highest, middle = middle, and low = lowest

#usage: python ascending_descending.py -f [codeML results file to analyze]

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='make files of those orthogroups whose dN/dS ratios either ascend or descend')
#add an argument that is the file to be parsed. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#add an argument that is the file to parse
args = parser.parse_args()

#open the file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    next(reader)
    listOfLists = list(reader)

high_medium_low = []
high_low_medium = []
medium_high_low = []
medium_low_high = []
low_high_medium = []
low_medium_high = []

for line in listOfLists:
    for i in range(1, 4):
        line[i] = float(line[i])
    if line[1] > line[2] and line[2] > line[3]:
        high_medium_low.append(line)
    if line[1] > line[3] and line[3] > line[2]:
        high_low_medium.append(line)
    if line[2] > line[1] and line[1] > line[3]:
        medium_high_low.append(line)
    if line[2] > line[3] and line[3] > line[1]:
        medium_low_high.append(line)
    if line[3] > line[1] and line[1] > line[2]:
        low_high_medium.append(line)
    if line[3] > line[2] and line[2] > line[1]:
        low_medium_high.append(line)

with open("high_medium_low.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(high_medium_low)

with open("high_low_medium.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(high_low_medium)

with open("medium_high_low.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(medium_high_low)

with open("medium_low_high.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(medium_low_high)

with open("low_high_medium.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(low_high_medium)

with open("low_medium_high.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(low_medium_high)
