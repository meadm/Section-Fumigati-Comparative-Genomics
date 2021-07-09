#!/bin/python
#this script will write files that have orthogroups whose dN/dS ratios either ascend or descend
    #ie high = highest, middle = middle, and low = lowest
    #and vice versa

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
    listOfLists = list(reader)

ascending = []
descending = []

for line in listOfLists:
    if line[2] > line[3] and line[3] > line[4]:
        descending.append(line)
    if line[2] < line[3] and line[3] < line[4]:
        ascending.append(line)


with open("descending.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(descending)

with open("ascending.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(ascending)
