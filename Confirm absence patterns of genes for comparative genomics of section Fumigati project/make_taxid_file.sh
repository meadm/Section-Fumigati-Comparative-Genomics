#for every fasta file in the directory...
for FILE in *.fna; do
        #cutoff the fna
        BEFOREDOT=$(echo $FILE| cut -d. -f1,1)
        #find all the contig IDS and save them to an intermediate file
        grep '>' $FILE | cut -c2- > dummy.txt
        #loop through that intermediate file line by line
        while read LINE; do
                #print the contig and then the file (strain) it is in
                echo $LINE $BEFOREDOT >> contig_strain.txt
        done < dummy.txt
done
