#USAGE:
#python consensus.py [ALIGNMENT IN CLUSTALFORMAT] [ALIGNMENT CUTOFF] > [OUTPUT FILE NAME]

import sys
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio import SeqIO

#save the file as an alignment object BioPython can parse
alignment = AlignIO.read(sys.argv[1], 'clustal')
summary_align = AlignInfo.SummaryInfo(alignment)
#make the consensus sequence
consensus = summary_align.dumb_consensus(threshold=float(sys.argv[2]), ambiguous="A")
#split the file name
file = sys.argv[1].split('.')
#print the file name/ID for the fasta
print('>' + file[0])
#print the consensus
print(consensus)
