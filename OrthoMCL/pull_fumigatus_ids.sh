#!/bin/bash
while read LINE; do
    #first grep finds the right orthogroup
    #first cut pulls everything after the orthogroup ID
    #sed converts the spaces (the delimiters) to new lines so that the second grep is easier
    #second grep finds only Af293 genes
    #second cut pulls just the AFUA ID
    grep "ORTHOMCL${LINE}" all_orthomcl.out | cut -f2,2 | sed -e 's/ /\'$'\n/g' | grep 'A_fumigatus_Af293' | cut -d'|' -f3,3
done < $1
