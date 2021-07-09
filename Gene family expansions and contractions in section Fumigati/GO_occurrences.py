#!/bin/python
#usage: python GO_occurrences.py [file to be parsed]
#will print how many times each GO term is in a file

#need sys to pass user inputs to script
import sys

#need csv to read in the tab-delimited file
import csv

#load inputs as an argument
input = sys.argv

#open file and make it a list of lists
with open(input[1]) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
lines = [x.strip() for x in content]

#GO_numbers will be a dictionary that contains GO terms as keys and the number of times that GO term is in the file as the value

GO_numbers = {}

for line in lines:
    #if the GO term is not in GO_numbers yet
    if line not in GO_numbers:
        #add that GO term to GO_numbers and set its value to 1
        GO_numbers[line] = 1
    #if that GO term is in GO_numbers and its value is 1
    else:
        #add one to that value
        GO_numbers[line] += 1

for i in GO_numbers:
    print(i + '\t' + str(GO_numbers[i]))
