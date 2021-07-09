.libPaths("~/R/rlib-3.6.0")
setwd('/scratch/meadm/Fumigati/ANOVA/PhylANOVA')
library(phytools)
newick_text = "(A_cejpii_FS110:0.1130052150,A_clavatus_NRRL1:0.1550605578,(((A_cristatus_GZAAS20.1005:0.0412743068,A_glaucus_CBS516.65:0.0470971681)100:0.3168503315,A_wentii_DTO134E9:0.2490996496)100:0.1967007943,(((((A_fischeri_NRRL181:0.0102588165,(((A_fumigatus_12-750544:0.0012083874,A_fumigatus_F16311:0.0018097995)100:0.0003202137,A_neoellipticus_NRRL5109:0.0031609841)98:0.0008248731,(A_fumigatus_A1163:0.0006062922,A_fumigatus_Af293:0.0007440382)100:0.0024012279)100:0.0340399748)100:0.0114496629,(A_lentulus_IFM54703:0.0238271160,A_novofumigatus_IBT16806:0.0232811889)100:0.0029638019)100:0.0139307492,(A_udagawae_IFM46973:0.0252516186,A_viridinutans_FRR_0576:0.0190022742)100:0.0091408630)100:0.0141519270,(A_turcosus_HMRAF1038:0.0017609445,A_turcosus_HMRAF23:0.0018385156)100:0.0357931964)100:0.0138137286,A_thermomutatus_HMRAF39:0.0270961425)100:0.1072280871)100:0.0507960081);"
phylo_tree = read.tree(text=newick_text)
midpoint_tree <- midpoint.root(phylo_tree)
orthogroups <-as.matrix(read.csv('only_changes_transposed.csv', row.names=1, header=T))
x <- as.matrix(read.csv("pathogenicity.csv", row.names=1, header=T))[,1]
output <- data.frame(OG = (character()), Pvalue = (numeric()), stringsAsFactors=FALSE)
for (i in colnames(orthogroups)) {
        print(i)
	output <- rbind.data.frame(output, c(i, phylANOVA(midpoint_tree, x, orthogroups[,i], posthoc=FALSE, nsim=10000)$Pf), stringsAsFactors=FALSE)
   }
warnings()
write.table(output, "raw_pvalues.csv", row.names=F, col.names=FALSE, sep=",")
