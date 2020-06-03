import statistics

def choosePivot(a,l,r,s):
  n = r-l
  first = l
  last = r-1
  mid = n//2-1 if n%2==0 else n//2
  if(s=="left"):
    return first
  if(s=="right"):
    return last
  if(s=="median"):
    return statistics.median([a[first],a[last],mid])

def swap(a,i,j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp

def partition(a,l,r):
  p=a[l]
  i=l+1
  for j in range(l+1,r+1):
      if(a[j]<p):
          swap(a,j,i)
          i+=1
  swap(a,l,i-1)
  
def quickSort(a,l,r):
  n = r-l
  if(n<=1):
    return
  p = l
  val = a[p]
  partition(a,l,r)
  quickSort(a,0,val)
  quickSort(a,val,r-1)

a = [5,3,6,2,4,1]
quickSort(a,0,len(a)-1)
print(a)