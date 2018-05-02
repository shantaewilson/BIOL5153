#! /usr/bin/env python3


#load required modules

import sys
import os
import re
import argparse
from Bio import SeqIO
import collections

def get_args():
        #create an ArgumentParser object('parser')
        parser = argparse.ArgumentParser()

        # add required/positional argument
        parser.add_argument("gff", help="name of GFF file")
        parser.add_argument("fasta", help="name of FASTA file")

        # parse the argument
        return parser.parse_args()


def parse_fasta():
        # open and read the FASTA file
        genome = SeqIO.read(args.fasta, 'fasta')
        return genome.seq


def reverse_comp(dna_seq):
    replacement1=dna_seq.replace('A','t')
    replacement2=replacement1.replace('T','a')
    replacement3=replacement2.replace('C','g')
    replacement4=replacement3.replace('G','c')
    return (replacement4.upper())

gff_file="watermelon.gff"
fsa_file="watermelon.fsa"

#open the files
gff_in=open(gff_file,'r')
fsa_in=open(fsa_file,'r')



#Creating dictionary
#key exon, value=sequence
exon_sequences={}

#key is gene name and value= concatenated sequence
gene_sequences={}

exon_sequences_ordered={}

#Declare a variable
genome=''

line_number=0

for line in fsa_in:
    #print(str(line_number) + ":" + line)

    line=line.rstrip('\n')

    if line_number > 0:
        genome+=line

    line_number+=1


#print(len(genome))

#close the file fsa
fsa_in.close()


cds     = ''
trna    = ''
rrna    = ''
intron  = ''
misc    = ''
repeats = ''
sequence=''


for line in gff_in:
    line=line.rstrip('\n')

    fields=line.split('\t')
    type=fields[2]
    strand=fields[6]

    start=int(fields[3])

    end=int(fields[4])
    #print(type, "\t", start,"\t", end)


# extracting gene name and the sequences
    if type=='CDS':
        breaks=fields
        attributes=fields[8].split(';')
        gene_name=attributes[0]
        #print(gene_name)

        sequence=genome[start-1:end]

        if strand=='+':
            exon_sequences[gene_name]=sequence
        else:
            complement_sequence=reverse_comp(sequence)
            exon_sequences[gene_name]=complement_sequence


#close the GFF file
gff_in.close()

# order the exon sequences
exon_sequences_ordered = collections.OrderedDict(sorted(exon_sequences.items()))


# exons of the same gene
for gene_features, sequences in exon_sequences_ordered.items():
        gene_name = gene_features.split(' ')
        if gene_name[1] in gene_sequences:
                gene_sequences[gene_name[1]] += sequences
        else:
                gene_sequences[gene_name[1]] = sequences


print('\n'+"printing the genes and their sequences \n")
for genes, sequences in gene_sequences.items():
        print(">" + genes +"\n" + sequences+ "\n")




