import numpy as np


# 1- Create a numpy array with the values ​​(10,15,30,45,60).

result = np.array([10,15,30,45,60])

# 2- Create numpy array with numbers between (5-15).
result = np.arange(5,15)

# 3- Create a numpy array between (50-100) by increasing by 5.
result = np.arange(50,100,5)

# 4- Create a 10-element array consisting of zeros.
result = np.zeros(10)

# 5- Create an array consisting of ones with 10 elements.
result = np.ones(10)

# 6- Generate 5 evenly spaced numbers between (0-100).
result = np.linspace(0,100,5)

# 7 - Generate 5 random integers between (10-30).
result = np.random.randint(10,30,5)

# 8- Generate 10 numbers between -1 and 1.
result = np.random.randn(10)

# 9- Create a random matrix between (10-50) in size (3x5).
result = np.random.randint(10,50,15).reshape(3,5)

# 10- Calculate the sum of row and column numbers of the produced matrix?
matris = np.random.randint(10,50,15).reshape(3,5)
print(matris)
# print(matris.sum(axis = 1))
# print(matris.sum(axis = 0))


# 11- What is the largest, smallest and average of the matrix produced?
result = np.max(matris)
result = np.min(matris)
result = np.average(matris)
result = np.mean(matris)

# 12- What is the index of the largest value of the matrix produced =
result = matris.argmax()
result = matris.argmin()

# 13- Select the first 3 elements of the array containing numbers between (10-20).
arr = np.arange(10,20)
# print(arr)
result = arr[0:3]


# 14- Print the elements of the generated array in reverse.
result = arr[::-1]

# 15- Select the first row of the generated matrix.
result = matris[0]

# 16- Which element is in the 2nd row and 3rd column of the produced matrix?
result = matris[1,2]

# 17 - Select the first element in all rows of the generated matrix.
result = matris[:,0]

# 18- Square each element of the generated matrix.
result = matris ** 2

# 19- Which of the matrix elements produced is a positive even number?
# Make the range between (-50, +50).
matris = np.random.randint(-50,50,15).reshape(3,5)

# evens = matris % 2 == 0
evens = matris[matris % 2 == 0]
result = evens[evens > 0]


print(evens)
print(result)


