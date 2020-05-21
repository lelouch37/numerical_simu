import time
import numpy as np


n = 100

A = [[float(i + j) for j in range(n)] for i in range(n)]
B = [[float(i + j) for j in range(n)] for i in range(n)]
C = [[float(0) for j in range(n)] for i in range(n)]

start_time = time.perf_counter()
##############################################
######### Pythonの2次元リストによる行列積 ##########
##############################################

for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] + B[k][j] 


##############################################

end_time = time.perf_counter()
print(end_time - start_time, " [sec]")


A = np.array(A)
B = np.array(B)

start_time = time.perf_counter()

##############################################
############## Numpyによる行列積 ###############
##############################################

C = np.dot(A, B)

##############################################

end_time = time.perf_counter()
print(end_time - start_time, " [sec]")