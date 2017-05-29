#!/usr/bin/python3
#import o arg parse para pedir argumentos
import argparse 
#importar da database a class Record
from database import Record
#import pickle para guardar informacao num ficheiro temporario
import pickle
#importar os diferentes modolos de parsar ficheiros
from fasta import fasta_parser
import csv_blast
import csv_enzyme
import csv_fpkm
import csv_foldchange
import csv_geneontology

# parser
parser = argparse.ArgumentParser(description="ck database")

#argument - type of file used
parser.add_argument("-csv", dest="infile", nargs="+", help="file imported")

#argument - type of function used(blast, fpkm, enzyme,etc)
parser.add_argument("-t", dest="typefile", help="type of file imported")

#argument - type of file to save the variables
parser.add_argument("-temp", dest="tempfile", help="temp file")

#
arg = parser.parse_args()

#make a function
def main(): 

	if not arg.tempfile:
		base_dic = {}
	else: 
		base_dic = pickle.load(open(arg.tempfile, "rb"))

	if arg.typefile in ["fpkm", "foldchange", "geneontology"]:
		infiles = arg.infile
	else:
		infiles = arg.infile[0]
	

	v = {"fasta": fasta_parser, "blast": csv_blast.csv_file, "enzyme": csv_enzyme.csv_file, "fpkm": csv_fpkm.csv_file, "foldchange": csv_foldchange.csv_file, "geneontology": csv_geneontology.csv_file}
		
	dic_filled = v[arg.typefile](infiles, base_dic)

	pickle.dump( dic_filled, open( "output_database", "wb" ))

main()

