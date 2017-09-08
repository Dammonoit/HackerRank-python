#this is python example to print a sequence to numbers.
#n=int(input());print(*range(1,n+1))  #no working in hackerrank
from __future__ import print_function
n = int(input())
for i in range(n):
  print (i+1,end="")
