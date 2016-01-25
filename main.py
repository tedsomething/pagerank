#!/usr/bin/python



def calculator(matrix, damping = 0.85, iterations = 100, delta=0.00001):
	nodes = check_outbound(matrix)
	size = len(nodes)

	# lets check for emty matrix
	if size == 0:
		return {}

	# minimal value
	min_value = (1.0 - damping)/size #value for nodes without inbound links
	
	# pagerank vector
	pagerank = [1.0/size for i in range(0, size)]	
		
	for i in range(iterations):
		diff = 0 # check difference in each iteration
		
		# check if any node has no outbound links then it should link to all other pages
		

		temp = list(pagerank) # temporary holder for pagerank

		# computes each node PageRank based on inbound links
		for j in range(0, size):
			rank = min_value # temporary rank holder (initate with damping)

			# transfer pagerank from each of incidents
			for k in range(0, size):
				# first check if we have a link
				if nodes[k][j] == 0:
					continue

				rank += temp[k] * damping / links(nodes, k)
			 
			# check the difference between latest iteration and previus one
			diff += abs(temp[j] - rank)

			# replace previus iteration pagerank with latest
			pagerank[j] = rank
		
		# now we should check combined difference between previus iteration and determine if we have accurate enough pagerank
		if diff < delta:
			break
	
	# return the pagerank vector containing pagerank of each node
	return pagerank


def links(matrix, node):
	size = len(matrix)
	total = 0

	for i in range(0, size):
		if matrix[node][i] == 1:
			total = total + 1

	return total


def check_outbound(matrix):
	size = len(matrix)

	for i in range(0, size):
		make = 0

		j = 0
		while j < size:
			if matrix[i][j] == 1:
				break

			if j == 1 and make == 0:
				j = 0
				make = 1

			if make == 1:
				matrix[i][j] = 1

			j = j + 1
	
	return matrix


def load(filename):
	lines = open(filename, "r").read().splitlines()
	
	matrix = []
	
	for line in lines:
		matrix.append(map(float, line.split("\t")))

	return matrix



# UI
calculator(load("test500.txt"))