#!/bin/python
#usage: tblastn.py -f [file containing OGs and taxa to check]

#need csv for opening the file
import csv

#allows you to run commands on the shell
import os

#needed for parsing the tblastn output files
import pandas as pd

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='runs tblastn to confirm proteins are missing from a set of genomes and makes a new file with results that have hits with percent identity >= 30% and coverage of the query >= 70%')
#add an argument that is the file containing the OGs and genome ids to be check. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the OG and taxa file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    l = list(reader)

#for every line in the list
for line in l:
    
    #variable that is just the orthogroup name
    og = line[0]
    
    #variable that is just the first taxa id to be checked for this orthogroup
    taxa=line[1]
    
    #if the number of taxa to check is greater than one...
    if len(line) > 2:
        
        #for every taxa id from the second one to the last one in the list on that line...
        for end in line[2:]:
            #add it to the taxa variable, separated by a comma
            taxa += ',' + end
    
    #variable that contains the name of the query file
    query = '../' + og + '/' + og + '.faa'
    
    #variable that is the output file name
    out = '../' + og + '/' + og + '.tblastn'
    
    #variable that contains the tblastn command
    cmd = "tblastn -db ../../Jacobs_genomes/all_in_one_stripped.fna -query " + query + " -outfmt '10 qaccver saccver pident length qlen evalue' -evalue 1e-10 -out " + out + " -taxids " + taxa
    
    #run the tblastn command
    os.system(cmd)
    
    #variable that will be the name of the filtered output file
    filtered = out + '.filtered'
    
    #pandas dataframe of the tblastn output that has all the lines and has headers
    df = pd.read_csv(out, header=None, names = ['qaccver', 'saccver', 'pident', 'length', 'qlen', 'evalue'])
    
    #add a column to the dataframe that contains the length of the alignment divided by the query length (aka the coverage of the hit)
    df['Coverage'] = df['length']/df['qlen']
    
    #filter the dataframe for percent identity greater than 30% and the coverage being greater than 70%
    #also print the filtered dataframe to a file that has tab-delimited columns
    df[(df.pident >= 30) & (df.Coverage >= 0.7)].to_csv(filtered, header=None, index=None, sep='\t')
    
    #print to the screen when the final file for this orthogroup is made
    print(filtered + ' is done!')
