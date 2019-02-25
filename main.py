from display import *
from draw import *
from matrix import *
import math

def shift_back(matrix,point):
	for col in range(len(matrix)):
		for row in range(len(matrix[0])-1):
			matrix[col][row] += point[row]

def shift_to(matrix,point):
	for col in range(len(matrix)):
		for row in range(len(matrix[0])-1):
			matrix[col][row] -= point[row]
def rotate(matrix,theta,point):
	if point != None:
		shift_to(matrix,point)
	m2 = new_matrix()
	ident(m2)
	m2[0][0] = math.cos(math.radians(theta))
	m2[0][1] = math.sin(math.radians(theta))
	m2[1][0] = -1 * math.sin(math.radians(theta))
	m2[1][1] = math.cos(math.radians(theta))
	# print_matrix(m2)
	matrix_mult( m2, matrix )
	for col in range(len(matrix)):
		for row in range(len(matrix[0])):
			matrix[col][row] = int(matrix[col][row])
	for col in matrix:
		col[len(matrix[0])-1] = 1
	if point != None:
		shift_back(matrix,point)

# Main begins here:
screen = new_screen()
color = [ 255, 128, 0 ]

test = new_matrix()

print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6)")
add_edge(test,1,2,3,4,5,6)
print_matrix(test)

print("Testing ident on matrix test:")
ident(test)
print_matrix(test)

m1 = new_matrix()
add_edge(m1,1,2,3,4,5,6)
add_edge(m1,7,8,9,10,11,12)
print("New matrix m1 is defined:")
print_matrix(m1)

print("Testing matrix_mult of m1 and identity")

matrix_mult(test,m1)
print_matrix(m1)


print("Testing matrix_mult for row operation (should switch rows 1 and 2")
test[1][1] = 0
test[1][2] = 1
test[2][2] = 0
test[2][1] = 1
matrix_mult(test,m1)
print_matrix(m1)

# For gallery image:
matrix = new_matrix()
# add_edge( matrix, 0, 250, 0, 250, 500, 0)
# add_edge( matrix, 250, 500, 0, 500, 250, 0)
# add_edge( matrix, 500, 250, 0, 250, 0, 0)
# add_edge( matrix, 250, 0, 0, 0, 250, 0)
add_edge( matrix, 0, 0, 0, 0, 500, 0)
add_edge( matrix, 0, 500, 0, 500, 500, 0)
add_edge( matrix, 500, 500, 0, 500, 0, 0)
add_edge( matrix, 500, 0, 0, 0, 0, 0)

# print_matrix(matrix)
point = [250,250,0,1]
for i in range(1000):
	rotate(matrix,5,point)
	draw_lines( matrix, screen, color)
# display(screen)
save_extension(screen, 'img.png')
