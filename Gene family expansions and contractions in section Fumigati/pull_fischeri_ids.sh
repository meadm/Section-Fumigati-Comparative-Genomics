#!/bin/bash
while read LINE; do
    #first grep finds the right orthogroup
    #first cut pulls everything after the orthogroup ID
    #sed converts the spaces (the delimiters) to new lines so that the second grep is easier
    #second grep finds only A. fischeri genes
    #second cut pulls just the NFIA ID
    grep -w "ORTHOMCL${LINE}" $2 | cut -f2,2 | sed -e 's/ /\'$'\n/g' | grep 'A_fischeri_NRRL181' | cut -d'|' -f3,3
done < $1
