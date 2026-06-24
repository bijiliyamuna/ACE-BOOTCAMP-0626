#  Arithmetic (operators and functions)
# Scalar Arithmetic (operations performing using single value)
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr+2) # Addition
print(arr-2) # Subtraction
print(arr*2) # Multiplication
print(arr/2) # Division
print(arr//2) # Floor Division
print(arr%2) # Modulo
print(arr**2) #Exponent
# Scalar Arithmetic Functions
print(np.add(arr,2))
print(np.subtract(arr,2))
print(np.multiply(arr,2))
print(np.divide(arr,2))
print(np.floor_divide(arr,2))
print(np.mod(arr,2))
print(np.power(arr,2))
print(np.sum(arr))
# Vector Arithmetics
arr1=np.array([[1,2,3],
               [1,5,6],
               [1,2,3]])
print(np.sum(arr1,0))
print(np.sum(arr1,1))
