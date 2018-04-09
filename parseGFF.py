#!/usr/bin/env python3

from Bio import SeqIO

# read in genome and store in a variable
for genome in SeqIO.parse("/users/qkward/Desktop/watermelon_files/watermelon.fsa", "fasta"):
	#print (genome.seq)
	genome = genome.seq


# open the GFF file
GFF_file = "/users/qkward/Desktop/watermelon_files/watermelon.gff"
GFF_in = open(GFF_file, 'r')

import sys
for line in GFF_in:
# split string into list
        coordinates = line.split("\t")
        start = int(coordinates[3])
        end = int(coordinates[4])
        org_name = (coordinates[0])
       # print(org_name)
        gene_name = (coordinates[8])
       # print(gene_name)
        print(org_name + gene_name + genome[start:end])

# close GFF file
GFF_in.close()
