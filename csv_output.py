#!/usr/bin/python3

import pickle
from sys import argv

dic_inst= pickle.load(open("output_database", "rb"))

blast_order = ["description", "seq_length", "evalue", "sim_mean"]
enzyme_order = ["Pathway", "Seqs_in_Pathway", "Enzyme", "EnzymeID", "EnzymeNr", "Pathway_ID", "Maps"]
fpkm_order = ["R24hr1", "R24hr2", "R48hr1", "R48hr2", "R72hr1", "R72hr2", "S24hr1", "S24hr2", "S48hr1", "S48hr2", "S72hr1", "S72hr2"]
gene_ontology_order = ["Biological_process", "Molecular_function","Cellular_component"]
gene_ontology_keys_order = ["term", "percentage", "num_seq"]
fold_change_order =  ["R24h48h", "R48h72h", "R24h72h", "S24h48h", "S48h72h", "S24h72h", "R24hS24h", "S48hR48h", "R72hS72h"]
fold_change_keys_order = ["PPEE", "PPDE", "PostFC", "RealFC", "log2FC", "exp_desc"]


def writeout (k, v):
	#add sequence ID 
	outline = k + ";"

	#add sequence to the table
	outline += dic_inst[k].sequence[0] + ";"

	#add kegg information to the table
	outline += ",".join(dic_inst[k].kegg_results) + ";"

	#add kogg information to the table
	outline += ",".join(dic_inst[k].kogg_results) + ";"

	#add kogg sub informtation to the table
	outline += ",".join(dic_inst[k].kogg_results_sub) + ";"

	#add blast information to the table
	for a in blast_order:
		outline += dic_inst[k].blast_results[a] + ";"

	#add enzyme results to the table
	for a in enzyme_order:
		v = dic_inst[k].enzyme_results[a]
		if not v:
			outline += ";"
		else:
			outline += ",".join(v) + ";"

	#add gene ontology results to the table 
	for a in gene_ontology_order:
		for b in gene_ontology_keys_order:
			v1= dic_inst[k].gene_ontology[a][b]
			if not v1:
				outline += ";"
			else:
				outline += ",".join(v1) + ";"


	#add fpkm results to the table
	for a in fpkm_order:
		v = dic_inst[k].fpkm_results[a]
		if v == []:
			outline += ";"
		else:
			outline += v +";"

	#add fold change results to the table
	for a in fold_change_order:
		for b in fold_change_keys_order:
			v1= dic_inst[k].fold_change[a][b]
			if v1 == []:
				outline += ";"
			else:
				outline += v1 +";"

	outline += "\n"
	#print(outline)
	outfile.write(outline)

outfile = open(argv[1], "w")
outfile.write("Locus_ID;sequence;kegg;Kogg;kogg_sub;description;seq_length;evalue;sim_mean;Pathway;Seqs_in_Pathway;Enzyme;EnzymeID;EnzymeNr;Pathway_ID;Maps;term;percentage;num_seq;term;percentage;num_seq;term;percentage;num_seq;R24hr1;R24hr2;R48hr1;R48hr2;R72hr1;R72hr2;S24hr1;S24hr2;S48hr1;S48hr2;S72hr1;S72hr2;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc;PPEE;PPDE;PostFC;RealFC;log2FC;exp_desc\n")

for k, v in dic_inst.items():
	writeout(k, v)

outfile.close()


