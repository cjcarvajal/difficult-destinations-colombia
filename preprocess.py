import json
file_path = '/Users/carlosj/Documents/Maestria/Visual Analytics/Homework-5/flights.json'

flights_data = {}

with open(file_path) as data_file:
	flights_data = json.load(data_file)

localities = set()
nodes = []
links = []
properties_file_name = 'tree_data.json'

for row in flights_data['data']:
	localities.add(row[8])
	links.append({'source':row[8],'target':row[9],'value':row[11]})

for locality in localities:
	nodes.append({'id':locality})

with open(properties_file_name, 'w') as outfile:
	json.dump({'nodes':nodes,'links':links}, outfile)