"""Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0"""



#Time complexity O(N^2)

def zero_matrix(matrix):
	M = len(matrix)
	N = len(matrix[0])
	index1 = []
	index2 = []
	for i in range(M):
		for j in range(N):
			if matrix[i][j] == 0:
				index1.append(i)
				index2.append(j)
	while len(index1) != 0:
		i = index1.pop()
		j = index2.pop()
		for k in range(N):
			matrix[i][k] = 0
		for m in range(M):
			matrix[m][j] = 0
	return matrix

if __name__ == '__main__':
  matrix = [[1, 2, 3, 4, 5],
            [6, 7, 0, 8, 9],
            [10, 11, 12, 13, 14]]
  print(zero_matrix(matrix))
