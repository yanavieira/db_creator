#!/usr/bin/python3
import csv

#open csv file
def csv_file (filename, dic_inst):
	try:
		f1= open(filename)
		cvs_f1 = csv.reader (f1)
	except IOError:
		print("The file, %s, does not exist" % filename)
		return 

	#keep the first line of the file
	next(f1)
	
	# parse csv file
	for line in f1:

		#split the line
		x= line.split (",")

		#add different elements to the list
		seq_id = x[0].strip()
		path = x[1]
		seqs_path = x[2]
		ez = x[3]
		ezID = x[4]
		ez_num= x[5]
		pathID = x[6].strip()

		#add information to the main file 
		obj = dic_inst[seq_id]

		obj.add_enzymeresults(path, seqs_path, ez, ezID, ez_num, pathID)

	return dic_inst

