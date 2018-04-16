#!/usr/bin/env python3

#load the required modules
import argparse
from Bio import SeqIO

#create an ArgumentParser object ('parser') that will hold the information necessary to parse the command line
parser = argparse.ArgumentParser(description="This script filters sequences from FASTA file that are shorter than a user-specified length cutoff")

#use add_argument() method to add a positional argument
#positional arguments are *required* inputs, so their order/position matters
#argparse treats all options as strings unless told to do otherwise
parser.add_argument("fasta",help="name of FASTA file")

#add an optional argument, the length cutoff for our filter
parser.add_argument("-m", "--min_seq_length", help="filter sequences that are >= min seq_length in length (default = 300 nt)", type=int, default=300)

#parse the arguments
args = parser.parse_args()


print("We're gonna open this FASTA file:", args.fasta)
print("filter sequences less than", args.min_seq_length, "nt in length")


for record in SeqIO.parse("watermelon_genes.fa", "fasta"):
        if len(record.seq) >= args.min_seq_length:
               print(record.format("fasta"))


