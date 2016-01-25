#!/usr/bin/python



def multiply(A, B, damping):
	C = [] # matrix that will hold final result
	length = len(A)
	diff = 0

	# rows of first matrix
	for i in range(length):
		temp = 0

		# columns of first matrix and rows of second
		for k in range(length):	

			# calculate matrix and vector
			temp += A[i][k] * B[k][0]

		# add damping
		temp += damping
		diff += abs(temp - B[i][0])

		C.append([temp])

	return C, diff

def calculate(pagerank, transitions, damping, iterations, delta):
	# get the new rank (main part of whole program that gets repeated)
	new, diff = multiply(transitions, pagerank, damping) # + damping

	# check difference
	if diff > delta:
		return calculate(new, transitions, damping, iterations, delta)
	else:
		return new

def load(filename):
	# this is suppose to be fast
	with open(filename, "r") as file:
		matrix = [map(int, line.split('\t')) for line in file]

	return matrix

def flip(matrix, size):
	new = [[] for i in range(size)]

	for i in range(size):
		for j in range(size):
			new[j].append(matrix[i][j])

	return new

def outlinks(matrix, damping, size):
	# holds damping that is divider by outlinks count of each node
	# this is done for speed
	vector = [(damping / sum(matrix[i])) for i in range(size)]

	return vector

def transitions(matrix, outlinks, size):
	# holds all node outlink count
	for i in range(size):
		for j in range(size):
			matrix[i][j] *= outlinks[j]

	# print matrix

	return matrix


def main(matrix, damping = 0.85, iterations = 100, delta = 0.00001):
	# total number of nodes
	size = len(matrix)

	# to use same test cases for each code sample we must flip test matrix
	# this adds some speed overhead so be warned
	new = flip(matrix, size)

	# initial page rank that is equal for each node
	pagerank =  [[(float(1)/float(size))] for i in range(size)]

	# this inverted damping that is going to be added to calculated vector
	# random factor
	vector_damping = ((1 - damping)/float(size))

	# this is computed transitions matrix that is going to be multiplied each iteration with page rank
	computed = transitions(new, outlinks(matrix, damping, size), size)

	# start recursive calculations
	return calculate(pagerank, computed, vector_damping, iterations, delta)

# UI
print main(load("tests/test10.txt"))
