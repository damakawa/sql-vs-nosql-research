from pymongo import MongoClient

client = MongoClient('mongodb://lanaeBK:bioinfo4thewin@ds145667.mlab.com:45667/pubmed-data')
db = client['pubmed-data']
collection = db.genes 

infile = open('gene-table.txt') 

for line in infile:
	count = 0
	symbol = ''
	name = ''
	for word in line.split('\t'):
		if count ==	1:
			symbol = word
		if count == 2:
			name = word
			mongodoc = {"symbol" : symbol, "name" : name}
			collection.insert(mongodoc)
		count += 1
		
client.close()