crime_type = ["ASSAULT","ROBBERY","THEFT OF VEHICLE","BREAK AND ENTER","THEFT FROM VEHICLE"]
crimecount = 0
type_id = {}#a dict that mapping from crime types to id
id_count={}#a dict that mapping from id to count

import string
fin = open("words.txt")
def get_type_id(file):
    for line in fin:
        wordlist = line.strip()
        wordlist1 = wordlist.split(',')
        print(wordlist1)
        for word in wordlist1:
            if word in type_id:
                type_id[word] = 1 + type_id.get(word,0)



for key in type_id:
    print(key)
    print(type_id[k])
        

def get_id_count(file):
	for value in type_id.values():
		id_count[value] = 1 + id_count.get(value,0)
	return id_count

def print_format(dict1,dict2):
	for key in dict1:
		a = dict1[k]
		print(key,dict[key],dict2[a])
		
dict1=get_type_id("words.txt")
dict2=get_id_count("words.txt")
print_format(dict1,dict2)

