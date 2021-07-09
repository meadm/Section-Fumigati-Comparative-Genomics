#!/bin/python
#this script will take an argument that represents which species are present in the orthogroup and print all orthogroups that match that pattern (ex. all species or all Fumigati or all A. fumigatus)

#usage: python species_of_interest.py -f [dupliPHY-ML file to analyze] -s [18 digit species representation ex. 001111101111110]

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='print only those orthogroups whose gene contents varies across columns in the file')
#add an argument that is the file to be parsed. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#add an argument that is the species representation
parser.add_argument("-s","--species",help="species to search for")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    listOfLists = list(reader)

for line in listOfLists:
    lineSpecies = ''
    for number in line[1:]:
        if int(number) > 0:
            lineSpecies += str(1)
        else:
            lineSpecies += str(0)
    if lineSpecies == args.species:
        print(line[0])
