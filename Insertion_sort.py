import numpy as np
from timeit import  default_timer as timer


def insertion_sort(A):
   for j in range(1,len(A)):
     #print(A)
     key=A[j]
     i=j-1
     while i>=0 and A[i]>key:
        A[i+1]=A[i]
        i=i-1
     A[i+1]=key


