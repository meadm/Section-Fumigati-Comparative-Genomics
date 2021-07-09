#!/bin/python
#this script will print the first 16 columns from lines of interest in a DupliPHY output file
#ie the number of genes in each species from the orthogroup of interest

#usage: python pull_orthogroups.py -f [DupliPHY file] -i [file of orthogroup deignations to pull]

#need csv for opening the files
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='Print the first 16 columns from lines of interest in a DupliPHY output file')
#add an argument that is the DupliPHY summary file. can use either "-f" or "--file"
parser.add_argument("-f","--file",help="DupliPHY-ML file")

parser.add_argument("-i","--interest",help="single column file of orthogroup designations of interest")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the DupliPHY file and make a dictionary that is each orthogroup designator (the first entry) as the key and every number after that as a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    l = list(reader)
    #for every row in l (the file), make a dictionary entry that is the first value (the orthogroup) as the key and all the other numbers as a list
    d = {row[0]:row[1:] for row in l}

#open file that contains list of orthogroups of interest and save those orthogroup designations to a list
with open(args.interest) as mainfilehandle:
    l = mainfilehandle.read().splitlines()

#for every orthogropu designation, print the orthogroup designation and the next 15 numbers, separated by commas
for i in l:
    string = ",".join(d[i][0:15])
    print(i + "," + string)
