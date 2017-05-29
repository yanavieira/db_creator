#!/usr/bin/python3

#Importar do modolo database a class Record

from database import Record

#open the Fasta file
def fasta_parser (filename, dic_inst):
	try:
		f= open(filename)
	except IOError:
		print("The file, %s, does not exist" % filename)
		return 

	name_list = []
	sequences = {}

#parse a fasta file 
	for line in f:
		if line.startswith(">"):
			name = line[1:].rstrip("\n")
			name_list.append(name)
			sequences[name] = ""
		else:
			sequences[name] += line.rstrip("\n")

	for k, v in sequences.items():
		#make an instance of a class Record for each sequence
		inst = Record(k)

		#make an dic with an instance of each sequence of the class Record 
		dic_inst[k] = inst

		#add information to the main file 
		dic_inst[k].add_seq(v)

#retomar o dicionario instantaneo 
	return dic_inst
