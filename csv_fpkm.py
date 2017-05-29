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

		#keep the first line of the file
		next(f1)

		# parse csv file
		for line in f1:

			#split the line
			x= line.split (",")

			#add different elements to the list
			seq_id = x[0].strip().strip('"')
			kogg = x[1].strip().strip('"')
			kogg_sub = x[2].strip().strip('"')
			kegg = x[3].strip().strip('"')
			R24h1 = x[4].strip().strip('"')
			R24h2 = x[5].strip().strip('"')
			R48h1 = x[6].strip().strip('"')
			R48h2 = x[7].strip().strip('"')
			R72h1 = x[8].strip().strip('"')
			R72h2 = x[9].strip().strip('"')
			S24h1 = x[10].strip().strip('"')
			S24h2 = x[11].strip().strip('"')
			S48h1 = x[12].strip().strip('"')
			S48h2 = x[13].strip().strip('"')
			S72h1 = x[14].strip().strip('"')
			S72h2 = x[15].strip().strip('"')

			#add information to the main file 
			obj = dic_inst[seq_id]

			#add fpkm information

			obj.add_fpkmresults([R24h1, R24h2, R48h1, R48h2, R72h1, R72h2, S24h1, S24h2, S48h1, S48h2, S72h1, S72h2])

			#add kegg information
			obj.add_keggresults (kegg)

			# add kogg information
			obj.add_koggresults (kogg)

			#add kogg sub category information
			obj.add_koggresults_sub (kogg_sub)


		f1.close()
		
	return dic_inst
			


