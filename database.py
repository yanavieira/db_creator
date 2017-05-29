#!/usr/bin/python3

class Record(): 
	# Initiate the class

	def __init__(self, name):
		self.name = name

		# sequence - fasta 
		self.sequence = []

		# information fungi or pseudo_fungi
		self.description = []

		#storing blast results
		self.blast_results = {"description": [], "seq_length": [], "evalue": [], "sim_mean": []} 

		# kegg results
		self.kegg_results = []

		# Kogg results category
		self.kogg_results =  []

		# Kogg results subcategory
		self.kogg_results_sub = []

		# Enzyme information - sera possivel colocar o link para o mapa?
		self.enzyme_results = {"Pathway": [], "Seqs_in_Pathway": [], "Enzyme": [], "EnzymeID": [], "EnzymeNr": [], "Pathway_ID": [], "Maps": []} 

		# Go information 
		self.gene_ontology = {"Biological_process": {"term": [], "percentage": [], "num_seq": []}, "Molecular_function": {"term": [], "percentage": [], "num_seq": []}, "Cellular_component": {"term": [], "percentage": [], "num_seq": []}}

		# Fpkm values 
		self.fpkm_results = {"R24hr1": [], "R24hr2": [], "R48hr1": [], "R48hr2": [], "R72hr1": [], "R72hr2": [], "S24hr1": [], "S24hr2": [], "S48hr1": [], "S48hr2": [], "S72hr1": [], "S72hr2": []}

		# Fold change
		self.fold_change =  {"R24h48h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}, "R48h72h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}, "R24h72h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}, "S24h48h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}, "S48h72h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}, "S24h72h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}, "R24hS24h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}, "S48hR48h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}, "R72hS72h": {"PPEE": [], "PPDE": [], "PostFC": [], "RealFC": [], "log2FC": [], "exp_desc": []}}


	# add sequences to the file

	def add_seq(self, seq):

		if not self.sequence:
			self.sequence = [seq]
		else:
			#print("Repeated sequence detected", self.sequence)
			pass

	# add information about sequence orgin (Fungi or probabily fungi)

	def add_description(self, desc):

		self.description.append(desc)

	# add blast results to the sequence - best hit information 

	def add_blastresults(self, desc, length, ev, sim):

		self.blast_results["description"] = desc
		self.blast_results["seq_length"] = length
		self.blast_results["evalue"] = ev
		self.blast_results["sim_mean"] = sim

	# add kegg information to the sequence

	def add_keggresults (self, kegg):
		
		#confirmation of the results 

		if not self.kegg_results:
			self.kegg_results.append(kegg)
		else: 
			if self.kegg_results[0] == kegg:
				pass
			else:
				self.kegg_results[0] += " %s - error_kegg incongruency" % kegg 
 

	# add kogg information to the sequence

	def add_koggresults (self, kogg):

		#confirmation of the results 

		if not self.kogg_results:
			self.kogg_results.append(kogg)
		else: 
			if self.kogg_results[0] == kogg:
				pass
			else:
				self.kogg_results[0] += " %s - error_kogg incongruency" % kogg 

	# add kogg subcategory information to the sequence

	def add_koggresults_sub (self, kogg_sub):

		#confirmation of the results 

		if not self.kogg_results_sub:
			self.kogg_results_sub.append(kogg_sub)
		else: 
			if self.kogg_results_sub[0] == kogg_sub:
				pass
			else:
				self.kogg_results_sub[0] += " %s - error_kogg_sub incongruency" % kogg_sub  


	# add information about sequences with enzyme information

	def add_enzymeresults (self, path, seqs_path, ez, ezID, ez_num, pathID): 

		
		self.enzyme_results["Pathway"].append(path)
		self.enzyme_results["Seqs_in_Pathway"].append(seqs_path)
		self.enzyme_results["Enzyme"].append(ez)
		self.enzyme_results["EnzymeID"].append(ezID)
		self.enzyme_results["EnzymeNr"].append(ez_num)
		self.enzyme_results["Pathway_ID"].append(pathID)

	#add information about gene ontology
	def add_geneontology (self, gn_ont, vals):

		info = ["term", "percentage", "num_seq"]

		for k, v in zip(info, vals):
			self.gene_ontology[gn_ont][k].append(v)

	#add fpkm results
	def add_fpkmresults(self, res):

		keys = ["R24hr1", "R24hr2", "R48hr1", "R48hr2", "R72hr1", "R72hr2", "S24hr1", "S24hr2", "S48hr1", "S48hr2", "S72hr1", "S72hr2"]

		for k, v in zip(keys, res):

		#confirmation of the fpkm values beetween samplesheets
			if not self.fpkm_results[k]:
				self.fpkm_results[k]= v
			else:
				if self.fpkm_results[k] == v:
					pass
				else:
					self.fpkm_results[k] += "%s - error_fpkm value incongruency" % v 


	def add_foldchange (self, datasets, vals):

		info =["PPEE", "PPDE", "PostFC", "RealFC", "log2FC", "exp_desc"] 

		for k, v in zip(info, vals):

			#confirmation of the fpkm values beetween samplesheets
			if not self.fold_change[datasets][k]:
				self.fold_change[datasets][k] = v
			else: 
				if self.fold_change[datasets][k] == v:
					pass
				else:
			 		self.fold_change[datasets][k] += "%s - error_foldchange incongruency" % v




















		