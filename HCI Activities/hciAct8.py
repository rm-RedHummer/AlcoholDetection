'''myDictionary = {'a':[10,20,30], 'b':{'a':['x',4,'y'], 'j':[{'mango':5, 'grapes':37},{'great':'hello'},{'name': 'Greenie', 'country': ['Jamaica','Chile','Venezuela']}]}, 'd': ['house', 'ball']}

print myDictionary['a'][2]
print myDictionary['b']['a'][2]
print myDictionary['b']['j'][0]['grapes']
print myDictionary['b']['j'][2]['name']
print myDictionary['b']['j'][2]['country'][2]
print myDictionary['d'][0]'''

dnaDictionary = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S',
'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y',
'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L',
'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T',
'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K',
'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A',
'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D',
'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
'GGG': 'G'}

#print dnaDictionary['TTT']
dna = ""
dna = str(raw_input("Enter DNA sequence: "))
output = ""
for letter in range (0,len(dna),3):
	if len(dna[letter:letter+3])%3 == 0: 
		output = output + dnaDictionary[dna[letter:letter+3]] + " "
	else:
		output = output + "* "
print output