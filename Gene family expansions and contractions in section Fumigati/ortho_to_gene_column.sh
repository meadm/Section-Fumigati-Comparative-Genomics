while read LINE; do
	#grep the orthogroup, remove the orthogroup id, remove the weird first space after the orthogropu id, turn the spaces into newlines so that each gene is on a new line, remove the stuff in parenthesis that corresponds to the name of the protein file Jacob gave to OrthoMCL, and write that line to a file named after the orthogroup you're currently on	
	grep -w "ORTHOMCL${LINE}" $2 | cut -f2,2 | cut -d' ' -f2- | tr " " "\n" | cut -d'(' -f1,1 >> OG${LINE}.txt
done < $1
