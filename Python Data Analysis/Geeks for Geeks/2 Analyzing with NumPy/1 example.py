# creating an array
import numpy as np

b = np.empty(2,dtype = int)
print("Matrix b:\n",b)

a = np.empty([2,2],dtype = int)
print("\nMatrix b:\n",a)

c = np.empty([3,3])
print("\nMatrix c: \n",c)

# create Array using numpy zero 

import numpy as np
b = np.zeros(2,dype = int)
print('Matrix b : \n',a)

a = np.zeros([2,2],dtype = int)
print("\nMatrix a: \n",a)

c = np.zeros([3,3])
print('\nMatrix c:\n',c)


# Operations on Numpy 

# Aritmetic Operations

# Additon

import numpy as np

# Defining both the matrices

a = np.array([5,72,13,100])
b= np.array([2,5,10,30])

# Perfomring addition using arithmetic operaator
add_ans = a + b
print(add_ans)

# Performing addition using numpy function
add_ans = np.add(a,b)
print(add_ans)

# The same functions and operations can be used for
# muliple matrices

c = np.array([1,2,3,4])
add_ans = a + b + c
print(add_ans)

add_ans = np.add(a,b,c)
print(add_ans)      

 # subtraction
 import numpy as np
 
 # defining both the matrices
 a = np.array([5,72,13,100])
b= np.array([2,5,10,30])

# performing subtraction using arithmetci operator
sub_ans = a-b
print(sub_ans)

# perfomring subtraction using numpy function
sub_ans = np.subtract(a,b)
print(sub_ans)

# division
import numpy as np
 # Defining both the matrice
 a = np.array([5,72,13,100])
b=np.array ([2,5,10,30])


# Perfoming divison using arithmetics opertaprs
div_ans = a/b
print(div_ans)

# Perofmring division using numpy functions
div_ans = np.divide(a,b)
print(div_ans)

#Python Numpy Array Indexing

# Python program to demostrate
#The use of index arrays
import numpy as np

# create a sequence of intergers from
# 10 to 1 with a tep -2
a= np.arrange(10,1,-2)
print(a)

# indexes are specified inside the np.array method
newarr = a[np.array([3,1,2])]
print(newarr)


# Numpy Arrya Slicing
import numpy as np

# arrange elements from 0 to 19
a = np.arrange(20)
print(a)

# a[start : stop;step]
print(-a[8:17:1])

#The operator means all elemnets till the end
print(a[10:])