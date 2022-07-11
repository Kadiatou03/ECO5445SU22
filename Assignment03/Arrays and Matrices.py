import numpy as np

#Constructing the following array "A" with i = 3 rows and j = 4 columns: 

A = np.array([[1., 2., 3., 4.], [5., 6., 7., 8.], [9., 10., 11., 12.]])
print("A =", A)

i = len(A)
j = len(A[0])
print("i =",i, end=' ')
print("rows")

print("j =",j, end=' ')
print("columns")



#From array A, extract "number 7" 

A[1][2]

#From array A,"row 1"
A[0]

#From array A,"column 2"
A[: ,1]

#From array A,"rows 2 and 3" 
A[1], A[2]

#From array A, "values 7, 8, 11, and 12"
A[1][2], A[1][3], A[2][2], A[2][3]




#Create the array B = 2*A - 8. 
B = 2*A - 8.
print('B =', B)


# The sum of the row values
np.sum(B, axis=1) 

#    Optional verification: Display sum of each row 
print("Sum first row =", sum(B[0]))
print("Sum second row =",sum(B[1])) 
print("Sum third row =", sum(B[2]))

# The sum of the column values
np.sum(B, axis=0) 

#    Optional verification: Display sum of each column 
print("Sum first column =", sum(B [: ,0]))
print("Sum second column =",sum(B [: ,1])) 
print("Sum third column =", sum(B [: ,2]))
print("Sum fourth column =", sum(B [: ,3]))

# The cumulative sum of row values
np.cumsum(B, axis=1) 

#the cumulative sum of column values
np.cumsum(B, axis=0) 



#From array B, create new arrays containing the element-by-element: natural logarithm
l = np.log(B)
print(l)
      

#From array B, create new arrays containing the element-by-element: square root
sr = (np.sqrt(B))
print(sr)

#From array B, create new arrays containing the element-by-element: square
sq = (np.square(B))
print(sq)

#From array B, create new arrays containing the element-by-element: absolute value
ab = np.abs(B)
print(ab)





# Estimated linear demand and supply functions of pork in Canada. 
#         Q = 286 - 20p.
#         Q = 88 + 40p.

# Define first matrix 'v' using Numpy arrays
v = np.matrix([[1., 20.],[1., -40.]])

# Define second matrix 'w' using Numpy arrays
w = np.matrix([[286], [88]])

# Unknowns are Q and p in the linear equations

# Find the inverse of 'v'
v_inverse = np.linalg.inv(v)
print(v_inverse)

#Solving final answer 's'
s = v_inverse * w
print(s)

# The equilibrium price is 3.3 and equilibrium quantity is 220.



#         Optional verification 
q = 286 - 20*3.3
q1 = 88 + 40*3.3

#       Both should equal to 220
print(q)
# t=220
print(q1)
# t1=220
