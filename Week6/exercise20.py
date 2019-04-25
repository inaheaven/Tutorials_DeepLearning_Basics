import numpy as np

A = np.array([[1,2]])
B = np.array([[-2], [3]])
C = np.array([[3,2], [-1,0]])

print(A.dot(B))
print(A.dot(C))
print(B.dot(A))
print(C.dot(B))