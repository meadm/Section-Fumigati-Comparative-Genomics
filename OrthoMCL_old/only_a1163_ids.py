#!/bin/python
#this script will print species-specific proteins if given a list of protein ids and an orthoMCL file
#NOTE: THIS LIST OF "SPECIES-SPECIFIC PROTEINS" WILL NOT INCLUDE PARALOGS! (IE PARALOGOUS PROTEINS THAT ARE IN AN ORTHOGROUP BY THEMSELVES IN THE ORTHOMCL FILE)

#usage: python only_a1163_proteins.py -p [FILE THAT CONTAINS A COLUMN OF PROTEIN IDS OF INTEREST] -o [ORTHOMCL OUTPUT FILE]
#stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='How many and which Proteins are Species-specific')
#add an argument that is the network file. can use either "-f" or "--file"
parser.add_argument("-p","--protein",help="list of protein IDs")
parser.add_argument("-o","--orthomcl",help="orthoMCL output")
#pass all of these arguments to a variable you can then call later on in the script
args = parser.parse_args()

#open the file and make a list that is each line of the file
with open(args.protein) as mainfilehandle:
    proteome = [line.rstrip('\n') for line in mainfilehandle]

with open(args.orthomcl) as secondFileHandle:
    orthomcl = [line.rstrip('\n') for line in secondFileHandle]
    orthomcl = [line.rstrip('\t') for line in orthomcl]

#for every protein in the proteome, if it is in the orthoMCL file, move on
for i in proteome:
    if any(i in s for s in orthomcl):
        continue
    #if the protein isn't in the orthoMCL file, print it
    else:
        print(i)
