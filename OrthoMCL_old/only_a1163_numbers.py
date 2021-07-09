#!/bin/python
#this script will print how many A1163 proteins are in orthogroups
#this number does not inlude paralogs in A1163
    #ie orthogroups that only have A1163 genes in it

#usage: python only_a1163_numbers.py -f [DupliPHY-ML description table]

#need csv for opening the files
import csv

#stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='How many and which Proteins are Species-specific')
#add an argument that is the DupliPHY summary file. can use either "-f" or "--file"
parser.add_argument("-f","--file",help="DupliPHY-ML file")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the DupliPHY file and make a dictionary that is each orthogroup designator (the first entry) as the key and every number after that as a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    l = list(reader)
    #for every row in l (the file), make a dictionary entry that is the fist value (the orthogroup) as the key and all the other numbers as a list
    d = {row[0]:row[1:] for row in l}

#dInt will be a dictionary that has the same keys and values, but the values will now be integers instead of strings
dInt = {}

for k in d:
    dInt[k] = []
    #for every value in the list for d[k], convert it to an integer and add it to the new dictionary (dInt) that uses the same keys (orthogroup ids)
    for i in d[k]:
        new = int(i)
        dInt[k].append(new)

#raw is the number of total genes from A1163 in the file. Includes paralogs only in A1163
raw = 0

#add up all the raw number of A1163 genes
for k in dInt:
    raw += dInt[k][4]

#paralogs will contain the number of paralogous genes. Genes only in A1163
paralogs = 0

for k in dInt:
    check = True
    #for every value with a location between 0 and 3,
    for i in range(4):
        #if the value at that location is 0 (aka there aren't any genes in that species), keep going
        if dInt[k][i] == 0:
            continue
        #if not, break the loop and set check to False
        else:
            check = False
            break
    #if check is still set to true (aka there aren't genes in the first four genomes for that orthogroup) and there are at least 2 genes in A1163 from that orthogroup
    if check and dInt[k][4] > 1:
        #for every value with a location between 5 and 14 (aka the rest of the genome columns in the file)
        for i in range(5,15):
            #if the value at that location is 0 (aka there aren't any genes in that species), keep going
            if dInt[k][i] == 0:
                continue
            #if not, break the loop and set check to False
            else:
                check = False
                break
        #if check is still true (aka there are only paralogous genes in that orthogroup for A1163)
        if check:
            #add the total number of A1163 genes to the total number of paralogs
            paralogs += dInt[k][4]

#print the total number of A1163 genes in orthogroups minus the number of paralogous A1163 genes
print(raw-paralogs)
