#!/bin/bash
#$1 is the list of ids to pull
#$2 is the location of the all_orthomcl.out
while read LINE; do
    #first grep finds the right orthogroup
    #first cut pulls everything after the orthogroup ID
    #sed converts the spaces (the delimiters) to new lines so that the second grep is easier
    #second grep finds only A. novofumigatus genes
    #second cut pulls just the ID
    grep "ORTHOMCL${LINE}" $2 | cut -f2,2 | sed -e 's/ /\'$'\n/g' | grep 'A_novofumigatus_IBT16806' | cut -d'|' -f3,3
done < $1
