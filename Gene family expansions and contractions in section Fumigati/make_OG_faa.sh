while read LINE; do
	SPECIES=$(echo $LINE | cut -d'|' -f1,1)
	samtools faidx /data/rokaslab/meadm/Fumigati/Sequences/${SPECIES}_protein.MOD.faa "$LINE" >> $1.faa
done < $1
