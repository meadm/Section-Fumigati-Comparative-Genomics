#!/bin/bash
#find all virulence-related genes in a dN/dS summary file that Jacob gave me
while read LINE; do
#$2 is the list of virulence orthogroups
    ORTHOGROUP=$(echo $LINE | cut -d, -f1,1 | cut -c9-)
    if grep -q -w "$ORTHOGROUP" $2; then
        echo ${LINE},yes
    else
        echo "${LINE},no"
    fi
done < $1
#$1 is the dN/dS summary file from Jacob
