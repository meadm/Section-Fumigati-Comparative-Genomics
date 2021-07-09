#!/bin/python
#this script will identify orthogroups that differ by more than a user-supplied number of genes (ex. A. fumi has 4 copies of that orthogroup but A. fisc only has 1)

#usage: python big_differences.py -f [dupliPHY-ML file to analyze] -n [difference (or greater) between largest and smallest number of genes]

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='print only those orthogroup ids whose gene contents differ by the user-supplied number or more')
#add an argument that is the file to be parsed. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#add an argument that is the difference cutoff
parser.add_argument("-n","--number",help="difference cutoff")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    listOfLists = list(reader)

#for every line(entry) in the file(list of lists)...
for line in listOfLists:
    orthogroup = [line[0]]
    neo = [line[2]]
    newList = orthogroup + neo + line[5:10] + line[11:18]
    newList = [int(i) for i in newList]
    largest = max(newList[1:])
    smallest = min(newList[1:])
    difference = largest - smallest
    if difference >= int(args.number):
        print(",".join(line[0:]))
