from pymongo import MongoClient



def popDB(cancer):
	client = MongoClient('mongodb://lanaeBK:bioinfo4thewin@ds145667.mlab.com:45667/pubmed-data')
	db = client['pubmed-data']
	if cancer == 'bladder':
		collection = db.bladdercancer
	if cancer == 'lung':
		collection = db.lungcancer
	if cancer == 'pancreatic':
		collection = db.pancreaticcancer
	
	infile = open(cancer + '.txt') 

	for line in infile:
		pmid = 0
		title = ''
		authors = ''
		source = ''
		abstract = ''
		
		for chunk in line.split('\t'):
			description, content = chunk.split(':', 1)
			if description == 'PMID':
				pmid = int(content)
			elif description == 'Title':
				title = content
			elif description == 'Authors':
				authors = content
			elif description == 'Source':
				source = content
			elif description == 'Abstract':
				abstract = content
				mongodoc = {"pmid" : pmid, "title" : title, "authors" : authors, "source" : source, "abstract" : abstract}
				collection.insert(mongodoc)
			
	client.close()

######
#MAIN#
######
popDB('bladder')
popDB('lung')
popDB('pancreatic')