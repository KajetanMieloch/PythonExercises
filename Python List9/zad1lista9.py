import numpy as np
A = np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
B = np.array([6,2,-5,17,12])
X = np.linalg.solve(A,B)

print(" x= " + str(X[0]), " y= "+str(X[1])," z= "+str(X[2])," t= "+str(X[3])," u= "+str(X[4]))

