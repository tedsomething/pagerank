#!/usr/bin/python
import random

# size of matrix
MATRIX_SIZE = 5000

def generate(size):
	return [[random.randint(0, 1) for i in range(size)] for j in range(size)]

def save(matrix, filename):
	file = open(filename, "w")

	for line in matrix:
		file.write("\t".join(map(str, line)) + "\n")

# start
save(generate(MATRIX_SIZE), 'test' + str(MATRIX_SIZE) + '.txt')
