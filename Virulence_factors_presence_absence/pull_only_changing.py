#!/bin/python
#usage: pull_only_changing.py -f [CSV file to parse] > outputfile.csv

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='print only those orthogroups whose gene contents varies across columns in the file')
#add an argument that is the file to be parsed. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    l = list(reader)
    #for every row in l (the file), make a dictionary entry that is the first value (the orthogroup) as the key and all the other numbers as a list

#for every list in the list of lists...
for i in l:
    #first make a variable that will eventually tell us if the numbers in the list are all the same
    check = 'noChange'
    #for every entry in the list after the first one (aka for all the gene/presence absence numbers)...
    for j in i[1:]:
        #if the number you're on does NOT match the first number
        if j != i[1]:
            check = 'Change'
    if check == 'Change':
        # print(i)
        print(",".join(i[0:]))
