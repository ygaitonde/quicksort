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
     if(statistics.median([a[first],a[last],a[mid]]) == a[first]):
       return first
     if(statistics.median([a[first],a[last],a[mid]]) == a[last]):
       return last
     if(statistics.median([a[first],a[last],a[mid]]) == a[mid]):
       return mid
  
def swap(a,i,j):
  temp = a[i]
  a[i] = a[j]
  a[j] = temp
  
def partition(a,l,r,p_index):
  p = a[p_index]
  swap(a,l,p_index)
  i = l+1
  for j in range(l+1,r+1):
    global counter
    counter+=1
    if(a[j] < p):
      swap(a, i, j)
      i+=1
  swap(a,l,i-1)
  return a.index(p)

def quicksort(a,l,r):
  n = r-l
  if (n<1): return
  p = choosePivot(a,l,r,"r")
  j = partition(a,l,r,p)
  quicksort(a,l,j-1)
  quicksort(a,j+1,r)

with open('QuickSort.txt') as f:
    a = [x.strip() for x in f]
    a = [ int(x) for x in a ]
quicksort(a,0,len(a)-1)
print(counter)


#151001 comparison using m
#164123 comparison using r
#162085 comparison using l

