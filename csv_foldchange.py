#!/usr/bin/python3
import csv

#open csv file
dic_inst ={}
def csv_file (filelist, dic_inst):

	for filename in filelist:
		try:
			f1= open(filename)
			cvs_f1 = csv.reader (f1)
		except IOError:
			print("The file, %s, does not exist" % filename)
			return 

		datasets = filename.split(".")[0]

		#keep the first line of the file
		next(f1)
		
		# parse csv file
		for line in f1:

			#split the line
			x= line.split (",")

			#add different elements to the list
			seq_id = x[0].replace('"', '')
			PPEE = x[1].strip()
			PPDE = x[2].strip()
			PostFC = x[3].strip()
			RealFC = x[4].strip()
			Log2FC = x[5].strip()
			Exp_desc = x[6].strip()

			#print (seq_id, PPDE, PPEE, PostFC, RealFC, Log2FC, Exp_desc)
			#add information to the main file 
			#try works to add information to a sequencie with an instance
			try:
				obj = dic_inst[seq_id]

				#add fold change information
				obj.add_foldchange(datasets, [PPEE, PPDE, PostFC, RealFC, Log2FC, Exp_desc])	
							

			except KeyError:
				pass

	return dic_inst
