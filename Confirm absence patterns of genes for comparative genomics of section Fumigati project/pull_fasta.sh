#USAGE: sh pull_fasta.sh
#for every directory in the current directory
for DIRECTORY in */ ; do
	#make a variable that is just the OG ID (ie just the directory name with no "/"
	OG=$(echo $DIRECTORY | cut -d'/' -f1,1)
	#make a variable that is the long ID Jacob used in the protome fastas
	#grep the orthogroup, then turn the spaces into new lines (helps with grep'ing), then grep for just the AFUA (Af293) hits, then remove anything after the first parentheses (orthoMCL adds the file name to the end of the hits)
	FASTAID=$(grep -w "ORTHOMCL${OG}" ../all_orthomcl_rd2.out | tr ' ' '\n' | grep 'AFUA' | cut -d'(' -f1,1)
	#make a variable that is just the AFUA ID
	#print the long ID and cut out just the AFUA ID that will be inbetween the third and fourth pipes
	AFUA=$(echo $FASTAID | cut -d'|' -f3,3)
	#pull the fasta sequence for that AFUA gene and put it in the directory that has its OG ID	
	samtools faidx ../Jacobs_proteomes/A_fumigatus_Af293_protein.MOD.faa ${FASTAID} > ${OG}/${OG}_${AFUA}.faa
done
