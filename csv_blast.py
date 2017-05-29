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
		seq_id = x[0]
		desc = x[1]
		length = x[2]
		ev = x[3]
		sim = x[4].strip()

		#add information to the main file 
		obj = dic_inst[seq_id]

		obj.add_blastresults(desc, length, ev, sim)

	return dic_inst


