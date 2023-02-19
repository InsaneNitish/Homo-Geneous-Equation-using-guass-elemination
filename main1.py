import numpy a snp
import sys
n=int(input("enter the no. of variables : "))
a=np.zeroes((n,n+1))
x=np.zeroes(n)
print("Enter the cofficients of Augmented matrix : ")
for i in range(n):
  for j in range(n):
    a[i,j]=float