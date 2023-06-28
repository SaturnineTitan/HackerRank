import numpy

# Convert input from string to list (array) of integers 
A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))
# print inner and outer products 
print(numpy.inner(A, B))
print(numpy.outer(A, B))
