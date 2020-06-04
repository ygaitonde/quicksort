import statistics
counter = 0

def choosePivot(a,l,r,s):
  n = r-l
  first = l
  last = r
  mid = n//2-1 if n%2==0 else n//2
  if(s=="l"):
    return first
  if(s=="r"):
    return last
  if(s=="m"):
    return statistics.median([a[first],a[last],a[mid]])

def swap(a,i,j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp

def partition(a,l,r):
  p = a[l]
  i = l+1
  for j in range(l+1,r+1):
    if(a[j] < p):
      swap(a, i, j)
      i+=1
    global counter
    counter+=1
  swap(a,l,i-1)
  return i-1

def quicksort(a,l,r):
  if r-l<=1:
    return
  p = choosePivot(a,l,r,"l")
  swap(a,l,p)
  val = partition(a,l,r)
  quicksort(a,0,val-1)
  quicksort(a,val+1, r-l+1)

a = [6,5,12,4,3,2,1]
quicksort(a,0,len(a)-1)
print(a)
print(counter)