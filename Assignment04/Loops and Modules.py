import numpy as np 

# Set the number of points that would be generated as numPoints and the number of points in the circle as pointsInCercle equals to zero to start
numPoints = 1000000
pointsInCircle = 0 

# Use np.random.rand() function to help order data in a way what it is easier to manipulate and to organize data into array of points with coordinates (x,y)
p = np.random.rand(numPoints,2) 
print(p) 

# Loop through the array of points, where point is represented as array of 2 values, essentially x and y coordinates, then store first value as x and second value as y
# to compute the distance
for i in range(len(p)):
    x = p[i, 0]
    y = p[i, 1] 
    #print("x: ", x) 
    #print("y: ", y) 
    
# Distance is found by doing the squared root of (x*x + y*y) and as unit square circle where radius = 1, therefore distance from the point to origin has to be <= 1,
# if that is true, the point is in the circle and that increases the count of "pointsInCircle"
 
    distance = np.sqrt(x*x + y*y) 
    #print("distance: ", distance) 

    if distance <= 1: 
     pointsInCircle += 1 
     
# Wrote the pi formula and print the pi estimation     
     
pi = 4 * (pointsInCircle / numPoints) 
print("pi: ", pi)


# Different outputs generated by the code form my trials
#            pi:  3.132
#            pi:  3.152
#            pi:  3.1708
#            pi:  3.1356
