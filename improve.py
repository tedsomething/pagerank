#!/usr/bin/python



def calculator(matrix, damping = 0.85, iterations = 100, delta = 0.00001):
	size = len(matrix)

	# lets check for emty matrix
	if size == 0:
		return []

	# check of nodes that has no outlinks
	nodes = check_outbound(matrix, size)

	# get vector of outlink count for each node
	outlinks = outlink_vector(nodes, size)

	# minimal value
	min_value = (1.0 - damping)/float(size) #value for nodes without inbound links
	
	# pagerank vector (initiate equally)
	pagerank = [1.0/float(size)] * size
		
	for i in range(iterations):

		diff = 0 # check difference in each iteration

		temp = list(pagerank) # temporary holder for pagerank

		# computes each node PageRank based on inbound links
		for j in range(size):
			rank = min_value # temporary rank holder (initate with damping)

			# transfer pagerank from each of incidents
			for k in range(size):
				# first check if we have a link
				if nodes[k][j] == 0:
					continue

				rank += temp[k] * damping / outlinks[k]
			 
			# check the difference between latest iteration and previus one
			diff += abs(temp[j] - rank)

			# replace previus iteration pagerank with latest
			pagerank[j] = rank
		
		# now we should check combined difference between previus iteration and determine if we have accurate enough pagerank
		if diff < delta:
			break
	
	# return the pagerank vector containing pagerank of each node
	return pagerank


def outlink_vector(matrix, size):
	# holds all node outlinke count
	vector = [sum(matrix[i]) for i in range(size)]

	return vector


def check_outbound(matrix, size):
	for i in range(size):
		if sum(matrix[i]) > 0:
			continue

		if j == size - 1:
			matrix[i] = [1] * size

	return matrix


def load(filename):
	# this is suppose to be fast
	with open(filename, "r") as file:
		matrix = [map(int, line.split('\t')) for line in file]

	return matrix

# UI
print calculator(load("tests/test10.txt"))
