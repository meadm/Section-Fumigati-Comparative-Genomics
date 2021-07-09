#!/bin/python
#usage: python afua_to_afu.py -f [file containing AFUA ids to convert] -c [conversion table from FungiDB] -n [name of file that will contain the results]

#this script will take a file containing "AFUA" ids and convert them to "Afu" ids when given a conversion table (gene aliases) from FungiDB
import csv
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='Convert "AFUA" ids to "Afu" ids')
#add an argument that is the file that contains the list of ids you want to convert. can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to convert")
#add an argument that is a table that contains the conversion info from FungiDB
parser.add_argument("-c","--conversion",help="file that contains the conversion info: A \"gene aliases\" table from FungiDB")
#add an argument that is the file name that will contain the results
parser.add_argument("-n","--name",help="name for file that will contain the conversion results")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file with the original IDs
with open(args.file) as f:
    #make an empty list that will contain the AFUA ids
    to_convert=[]
    #for every line in the file
    for line in f:
        #strip off the new line information at the end
        stripped_line = line.rstrip()
        #and append that ID to the list
        to_convert.append(stripped_line)

#open the conversion file and make it a list of lists with each row being a list containing a list of the column values
with open(args.conversion) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter='\t')
    l = list(reader)

#make an empty list that will contain the results (Afu IDss)
results = []

#for every gene that needs to be converted...
for gene in to_convert:
    #make a variable that says the gene is NOT present in the conversion table
    present = False
    #for every line in the conversion table...
    for line in l:
        #if the gene you are currently on is in the line you are currently are on...
        if gene in line:
            #change the variable to say the gene IS present
            present=True
            #and append the Afu ID for the gene to the results list
            results.append(line[0])
    #if the gene is not present...
    if not present:
        #print to the screen that it is not present
        print(gene + ' ' + 'NOT PRESENT')

#write the file with the correct new line codes
with open(args.name, 'w') as filehandle:
    for listitem in results:
        filehandle.write('%s\n' % listitem)
