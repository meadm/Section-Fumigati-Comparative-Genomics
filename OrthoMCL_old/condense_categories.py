#!/bin/python
#need csv for opening the file
import csv

#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='in a DupliPHY-like row, change numbers to a given number if they are higher than or equal to the given number')
#add an argument that is the DupliPHY summary file. can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to simplify")

#add an argument that is the number you want to use as a benchmark - also sets this variable as an integer type instead of the default which is a string
parser.add_argument("-n","--number",help="number that if entry is greater than or equal to, the script will condense to", type=int)
#pass the argument to a variable you can then call later on in the script
args = parser.parse_args()

#open the DupliPHY-like file and make a dictionary that is each orthogroup designator (the first entry) as the key and every number after that as a list
with open(args.file) as mainfilehandle:
    reader = csv.reader(mainfilehandle, delimiter=',')
    l = list(reader)
    #for every row in l (the file), make a dictionary entry that is the first value (the orthogroup) as the key and all the other numbers as a list
    d = {row[0]:row[1:] for row in l}

#dInt will be a dictionary that has the same keys and values, but the values will now be integers instead of strings
dInt = {}

#for every value in the list for d[k], convert it to an integer and add it to the new dictionary (dInt) that uses the same keys (orthogroup ids)
for k in d:
    dInt[k] = []
    for i in d[k]:
        new = int(i)
        dInt[k].append(new)

#results will be a dictionary that contains the condensed numbers
results = {}

#for every key in the dictionary
for k in dInt:
    #make a new key in the results dictionary that is the key your loop is on
    results[k] = []
    #for every value in the dictionary with that key, if the value is larger than or equal to the number you gave the script, change that value in the results dictionary to the number you gave the script
    for v in dInt[k]:
        if v >= args.number:
            results[k].append(args.number)
        #if the value is less than the number you gave the script, copy that number over to the results dictionary
        else:
            results[k].append(v)

#final will be a dictionary that has the same info as results, except the values in the list will be strings instead of integers
#this will help with printing the values to standard output
final = {}
for k in results:
    final[k] = []
    for i in results[k]:
        new = str(i)
        final[k].append(new)

#for every key in the final dictionary, separate it and its list by commas and print it all to standard output
for i in final:
    string = ",".join(final[i][0:15])
    print(i + "," + string)
