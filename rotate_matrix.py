""" Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place? """



#time complexity O(N)
def rotate(matrix):
  length_inside = len(matrix)-1
  length_outside = int(len(matrix)/2)	
  for j in range(length_outside):
    for i in range(length_inside):
      matrix[j][i], matrix[i][len(matrix)-(1+j)] = matrix[i][len(matrix)-(1+j)], matrix[j][i]
      matrix[len(matrix)-(1+i)][j], matrix[j][i] = matrix[j][i], matrix[len(matrix)-(1+i)][j] 
      matrix[len(matrix)-(1+i)][j], matrix[len(matrix)-(1+j)][len(matrix)-(1+i)] = matrix[len(matrix)-(1+j)][len(matrix)-(1+i)], matrix[len(matrix)-(1+i)][j]  
      length_inside -= 2
    return matrix

if __name__ == '__main__':

  test = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
  test2 = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11,12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]
  test1 = [[1, 2, 3, 4, 5, 6],
          [7, 8, 9, 10, 11, 12],
          [13, 14, 15, 16, 17, 18],
          [19, 20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29, 30],
          [31, 32, 33, 34, 35, 36]]
  print(rotate(test))
