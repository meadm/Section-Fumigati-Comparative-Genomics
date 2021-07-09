#!/bin/python
#this script will take an argument that represents a p-value cutoff and returns only those orthogroups that had a p-value of that value or less

#usage: python p-value_cutoff.py -f [codeML results file to analyze] -p [p-value cutoff]

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='print only those orthogroups whose p-value are the provided value or less')
#add an argument that is the file to be parsed. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#add an argument that is the species representation
parser.add_argument("-p","--pvalue",help="pvalue cutoff")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    listOfLists = list(reader)

result = []
for i in listOfLists:
    number = float(i[1])
    if number <= float(args.pvalue):
        print(",".join(i[0:]))
