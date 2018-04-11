#!/usr/bin/env python3

# load the required modules
import argparse
from Bio import SeqIO


#create an ArgumentParser object ('parser') that will hold the information necessary to parse the command line
parser = argparse.ArgumentParser(description="This script accepts inputs from GFF and FASTA file")

# use add_argument() method to add a positional argument
#positional arguments are *required* inputs, so their order/position matters
#argparse treats all options as strings unless told to do otherwise
parser.add_argument("fasta",help="name of FASTA file")
parser.add_argument("gff",help="name of GFF file")


#parse the arguments
args = parser.parse_args()


print("We're gonna open this FASTA file:", args.fasta)
print("We're gonna open this GFF file:", args.gff)


# read in genome and store in a variable
for genome in SeqIO.parse("/users/qkward/Desktop/watermelon_files/watermelon.fsa", "fasta"):
	#print (genome.seq)
	genome = genome.seq


# open the GFF file
GFF_file = "/users/qkward/Desktop/watermelon_files/watermelon.gff"
GFF_in = open(GFF_file, 'r')

for line in GFF_in:
# split string into list
        fields = line.split("\t")
        start = int(fields[3])
        end = int(fields[4])
        org_name = (fields[0])
       # print(org_name)
        gene_name = (fields[8])
       # print(gene_name)
        print(org_name + gene_name + genome[start:end])

# close GFF file
GFF_in.close()
