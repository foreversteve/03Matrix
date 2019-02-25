"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
	for row in range(len(matrix[0])):
		line = []
		for col in matrix:
			line.append(col[row])
		print(line)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
	for col in range(len(matrix)):
		for row in range(len(matrix[0])):
			matrix[col][row] = 0
			if row == col:
				matrix[col][row] = 1


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
	col = 0
	for col in range(len(m1)):
		new_col = []
		for row in range(len(m1[0])):
			val = 0
			for count in range(len(m1)):
				val += m1[count][row] * m2[col][count]
			new_col.append(val)
		m2[col] = new_col

def new_matrix(rows = 4, cols = 4):
	m = []
	for c in range( cols ):
		m.append( [] )
		for r in range( rows ):
			m[c].append( 0 )
	return m



