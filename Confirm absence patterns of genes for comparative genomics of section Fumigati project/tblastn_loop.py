#!/bin/python
#usage: tblastn.py -f [file containing OGs and taxa to check]

#need csv for opening the file
import csv

#allows you to run commands on the shell
import subprocess

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='runs tblastn to confirm proteins are missing from a set of genomes')
#add an argument that is the file containing the OGs and genome ids to be check. Can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to parse")
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list of lists where each line is a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    l = list(reader)

for line in l:
    og = line[0]
    taxa=line[1]
    if len(line) > 2:
        for end in line[2:]:
            taxa += ',' + end
    query = '../' + og + '/' + og + '.faa'
    out = '../' + og + '/' + og + '.tblastn'
    command_line = ['tblastn', '-db', '../../Jacobs_genomes/all_in_one_stripped.fna', '-query', query, '-outfmt', '6', '-evalue', '1e-10', '-out', out, '-taxids', str(taxa)]
    subprocess.run(command_line)
