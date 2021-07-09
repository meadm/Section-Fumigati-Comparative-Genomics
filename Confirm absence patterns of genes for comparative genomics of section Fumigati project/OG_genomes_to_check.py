#!/bin/python
#usage: OG_genomes_to_check.py -f [CSV file to parse] > outputfile.csv

#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='take a dupliphyML output file and make a new file that has every OG and which species are missing from that OG')
#add an argument that is the file to be parsed. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    l = list(reader)

#make a list that contains all the possible strains that is in the same order as the orthoMCL output
species = ['ID', 'cejpii', 'neoellipticus', 'clavatus', 'cristatus', 'fischeri', '12', 'A1163', 'Af293', 'F16311', 'glaucus', 'lentulus', 'novofumigatus', 'thermomutatus', 'HMRAF1038', 'HMRAF23', 'udagawae', 'viridinutans', 'wentii']

#for every list (line) in the list of lists (file)
for i in l:
    #make a list that contains the results of the line the loop is currently on
    #have the first entry in the results list be the OG ID
    lineResults = [i[0]]
    #for every number in the range of 1-18
        #ie loop through the list
    for j in range(1, 19):
        #if any of the entries in the line are 0
        if i[j] == '0':
            #add that line to the results list
            lineResults.append(species[j])
    #print the results list as a csv
    print(",".join(lineResults))
