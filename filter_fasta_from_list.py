#!/usr/bin/env python3
#load the required modules
import argparse
import sys
from Bio import SeqIO

#create an ArgumentParser object ('parser') that will hold the information necessary to parse the command line
parser = argparse.ArgumentParser(description="This script filters sequences from FASTA file that are shorter than a user-specified length cutoff")

#use add_argument() method to add a positional argument
#positional arguments are *required* inputs, so their order/position matters
#argparse treats all options as strings unless told to do otherwise
parser.add_argument("fasta",help="name of FASTA file")

#add an optional argument, the length cutoff for our filter
#parser.add_argument("-m", "--min_seq_length", help="filter sequences that are <= min seq_length in length (default = 300 nt)", type=int, default=300)

parser.add_argument("list", help="a file with a list of sequence identifiers that will have identical matches to headers in the FASTA file")

#parse the arguments
args = parser.parse_args()

fasta = SeqIO.parse(args.fasta, "fasta")
print("We're gonna open this FASTA file:", args.fasta)
print("We're gonna open this FASTA file:", args.list)
#print("filter sequences less than", args.min_seq_length, "nt in length")

if len(sys.argv) < 3:

	print('Not enough args')

	sys.exit()

	

f = open(sys.argv[1], 'r')

data = f.read()



out = open(sys.argv[2], 'w')

while data:

	before,paren,data = data.partition('(')

	out.write(before)

	depth = 1

	i = 0

	while i < len(data) and depth:

		if data[i] == '(':

			depth += 1

		elif data[i] == ')':

			depth -= 1

		i += 1

	data = data[i:]
