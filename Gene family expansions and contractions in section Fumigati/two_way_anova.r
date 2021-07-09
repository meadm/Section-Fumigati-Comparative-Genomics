my_data <-read.csv('/scratch/meadm/Fumigati/ANOVA/input.csv')
my_data$orthogroup <-factor(my_data$orthogroup)
my_data$pathogenicity <- factor(my_data$pathogenicity)
res.aov2 <- aov(gene_number ~ orthogroup:pathogenicity, data=my_data)
tukey<-TukeyHSD(res.aov2)
test <- tukey[["orthogroup:pathogenicity"]]
write.table(test, file="output_orthogroup_pathogenicity.txt")
