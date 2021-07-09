#!/bin/sh
#this script will strip IDs in a fasta file for every fna file in a directory

for INPUT in *fna; do
#cut up the file name
	BEFOREDOT=$(echo $INPUT| cut -d. -f1,1)
	AFTERDOT=$(echo $INPUT | cut -d. -f2,2)
#strip the IDs of everything after the space	
	sed '/^>/ s/ .*//' $INPUT > ${BEFOREDOT}_stripped.${AFTERDOT}
	echo $INPUT DONE
done
