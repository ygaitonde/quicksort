import statistics
import random

def choosePivot(a,s):
  n = len(a)
  first = 0
  last = n-1
  mid = n//2-1 if n%2==0 else n//2
  if(s=="left"):
    return first
  if(s=="right"):
    return last
  if(s=="median"):
    return statistics.median([a[first],last,mid])

def swap(a,i,j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp

def partition(a, p):
  return
  
def quickSort(a):
  n = len(a)
  if(n==1):
    return
  p = random.choice(a)
  swap(a,0,p)
  partition(a,p)
  quickSort(a[0:p])
  quickSort(a[p:0])

a = [1,4,3,2,5,6]
quickSort(a)