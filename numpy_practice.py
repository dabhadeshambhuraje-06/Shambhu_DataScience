import numpy as np

#creating a array
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])

#displaying the array
print(a)
print(b)

#Array properties
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)
print("Data type of a:", a.dtype)
print("Data type of b:", b.dtype)
print("Size of a:", a.size)
print("Size of b:", b.size)
print("Dimension of a:", a.ndim)
print("Dimension of b:", b.ndim)

#Array arithmetic operations
#print("Addition:",a+b)
#print("Subtraction:",a-b)
#print("Multiplication:",a*b)
#print("Division:",a/b)
#print("Power:",a**2)

#scalar operations
print("Scalar addition:",a+5)
print("Scalar multiplication:",a*2)
print("Scalar division:",a/2)
print("Scalar subtraction:",a-5)

#comparison operations
print("Comparison a > 3:", a > 3)
print("Comparison a < 3:", a < 3)
print("Comparison a == 3:", a == 3)

#indexing and slicing
print("first element:", a[0])
print("last element:", a[-1])
print("slice:", a[1:4])
print("reverse:", a[::-1])

#array functions
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Standard deviation:", np.std(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("variance:", np.var(a))

#special arrays
print("Zeros:", np.zeros(5))
print("Ones:", np.ones(5))
print("Range:", np.arange(1, 11))
print("Even numbers:",np.arange(2,11,2))
print("Linear space:", np.linspace(0, 1, 5))

#matrix
matrix1 = np.array([[1, 2], [3, 4], [5, 6]])
matrix2 = np.array([[7, 8], [9, 10], [11, 12]])
print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)

#matrix properties
print("Shape of matrix1:", matrix1.shape)
print("Shape of matrix2:", matrix2.shape)
print("Data type of matrix1:", matrix1.dtype)
print("Data type of matrix2:", matrix2.dtype)
print("Size of matrix1:", matrix1.size)
print("Size of matrix2:", matrix2.size)
print("Dimension of matrix1:", matrix1.ndim)
print("Dimension of matrix2:", matrix2.ndim)

#matrix arithmetic operations
print("addition:", matrix1 + matrix2)
print("subtraction:", matrix1 - matrix2)
print("multiplication:", matrix1 * matrix2)
print("division:", matrix1 / matrix2)

#matrix multiplication
#print("Matrix multiplication:", np.matmul(matrix1, matrix2))
#print("Matrix multiplication using @:", matrix1 @ matrix2)

#Transpose
print("Transpose of matrix1:", matrix1.T)

#Diagonal
print("Diagonal of matrix1:", np.diag(matrix1))

#sum of rows and columns
print("Sum of rows:", np.sum(matrix1, axis=1))
print("Sum of columns:", np.sum(matrix1, axis=0))
print("Total sum:", np.sum(matrix1))

#maximum and minimum
print("Maximum:", np.max(matrix1))
print("Minimum:", np.min(matrix1))

#reshaping
x = np.arange(1,10)
print("Original array:", x)
print("Reshaped array:", x.reshape(3,3))

#Flatten
print("Flattened:", x.flatten())

#concatenation
print("Horizontal",np.concatenate((matrix1, matrix2), axis=1))
print("Vertical",np.concatenate((matrix1, matrix2), axis=0))

#sorting
unsorted_array = np.array([3, 1, 4, 2, 5])
print("Unsorted array:", unsorted_array)
print("Sorted array:", np.sort(unsorted_array))

#searching
print("Position where a>3:", np.where(a > 3))

#unique elements
c = np.array([1, 2, 2, 3, 4, 4, 5])
print("Unique elements:", np.unique(c))
