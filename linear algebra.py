import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[-2, 4], [1, 3]])
C = np.array([[2, -5], [3, -2]])
D = np.array([[5, -1, 3], [-4, 3, -6], [-3, 1, 2]])

#(a)
print(A[1, 1] + B[0, 0])

#(b)
print((A.T).T)

#(c)
print(B.T)

#(d)
print(A.T + B.T)

#(e)
print((A + B).T)

#(f)
print(3 * np.eye(2) - C)

#(g)
print(D - 5 * np.eye(3))

#(h)
#print((3 * np.eye(3)) * D) !!!행렬의 곱은 np.dot()이용!!!

print(np.dot(3 * np.eye(3),D))
