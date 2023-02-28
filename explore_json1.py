import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json','w')

#The json.load() function converts the data into a format Python 
#a giant dictionary
eq_data = json.load(infile)

#The json.dump() function takes a JSON data object and a file object file
#The indent=4 argument tells dump() to format the data using the data's structure.

json.dump(eq_data, outfile, indent=5)