import numpy

# Initialize coefficient list from input 
coefficients = numpy.array(list(map(float, input().split())))
# independent variable 
x = float(input())
# Evaluate function at x from given coefficients 
print(numpy.polyval(coefficients, x))
