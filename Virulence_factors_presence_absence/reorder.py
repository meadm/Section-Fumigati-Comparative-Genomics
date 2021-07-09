#!/bin/python
#this script will reorder the columns from an dupliphyML output so they match the section Fumigati phylogeny and sort the orthogroups so that they look pretty in a heatmap
import pandas as pd
#reads and stores the arguments
import argparse

#this first line is in all argparse setups - it gives the script a description for when you use "-h"
parser = argparse.ArgumentParser(description='reorder the columns from an orthoMCL output so they match the section Fumigati and sort the orthogroups so that they look pretty in a heatmap phylogeny')
#add an argument that is the counts file. can use either "-f" or "--file"
parser.add_argument("-f","--file",help="file to simplify")
#add an argument that is the output file name. can use either -o or --output
parser.add_argument("-o","--output",help="output file name")
#pass the arguments to a variable you can then call later on in the script
args = parser.parse_args()

#read in the counts file as a pandas dataframe and add column names
df = pd.read_csv(args.file, names=['FamilyID', 'A_cejpii_FS110', 'A_neoellipticus_NRRL5109', 'A_clavatus_NRRL1', 'A_cristatus_GZAAS20.1005', 'A_fischeri_NRRL181', 'A_fumigatus_12-750544', 'A_fumigatus_A1163', 'A_fumigatus_Af293', 'A_fumigatus_F16311', 'A_glaucus_CBS516.65', 'A_lentulus_IFM54703', 'A_novofumigatus_IBT16806', 'A_thermomutatus_HMRAF39', 'A_turcosus_HMRAF1038', 'A_turcosus_HMRAF23', 'A_udagawae_IFM46973', 'A_viridinutans_FRR_0576', 'A_wentii_DTO134E9'])

#reorder the columns so that they match the section Fumigati phylogeny
df = df[['FamilyID', 'A_fumigatus_12-750544', 'A_fumigatus_F16311', 'A_neoellipticus_NRRL5109', 'A_fumigatus_Af293', 'A_fumigatus_A1163', 'A_fischeri_NRRL181', 'A_lentulus_IFM54703', 'A_novofumigatus_IBT16806', 'A_udagawae_IFM46973', 'A_viridinutans_FRR_0576', 'A_turcosus_HMRAF23', 'A_turcosus_HMRAF1038', 'A_thermomutatus_HMRAF39', 'A_clavatus_NRRL1', 'A_cejpii_FS110', 'A_cristatus_GZAAS20.1005', 'A_glaucus_CBS516.65', 'A_wentii_DTO134E9']]

#sort the orthogroups (lines) so that they look good in a heatmap - highest count to lowest count
df = df.sort_values(by=['A_wentii_DTO134E9', 'A_glaucus_CBS516.65', 'A_cristatus_GZAAS20.1005', 'A_cejpii_FS110', 'A_clavatus_NRRL1', 'A_thermomutatus_HMRAF39', 'A_turcosus_HMRAF1038', 'A_turcosus_HMRAF23', 'A_viridinutans_FRR_0576', 'A_udagawae_IFM46973', 'A_novofumigatus_IBT16806', 'A_lentulus_IFM54703', 'A_fischeri_NRRL181', 'A_fumigatus_A1163', 'A_fumigatus_Af293', 'A_neoellipticus_NRRL5109', 'A_fumigatus_F16311', 'A_fumigatus_12-750544'], ascending=False)

#save the dataframe as a CSV, include the headers, but don't include the indexes on the side
df.to_csv(args.output, index = False, header=True)
