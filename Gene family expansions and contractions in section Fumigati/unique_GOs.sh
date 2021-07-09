#pull unique GO terms from an interproscan output
#for every tsv file in the directory (every interproscan output file)
for FILE in *tsv; do
    #make a new variable that is just the name of the orthogroup you're currently working on
    NEW=$(echo $FILE | cut -d_ -f1,1)
    #pull only the lines with GO annotations
    #from those lines only use the last entry (the GO annotations themselves)
    #translate the pipes to new lines (multiple GO annotations are separated by pipes in interproscan outputs)
    #sort for the unique GO annotations and write them to a file
    grep 'GO:' $FILE | awk '{print $NF}' | tr '|' '\n' | sort -u > ${NEW}_GO.txt
done
