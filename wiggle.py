#!/usr/bin/python 

def returnWiggled(arr):
      '''returns a wiggled sorted version of the list'''
      arr.sort()
      print arr
      n =len(arr)
      print n
      if  n<=2:
         return arr
      i=0 
      while(i<n-1):
          if (i+1)%2 != 0:
              #check for less than operation between a[i] and a[i+1]
               if a[i]<=a[i+1]:
                  i=i+1
                  continue 
               else: 
                  temp = a[i] 
                  a[i] = a[i+1]
                  a[i+1] = temp 
          if (i+1)%2 == 0:
             #check for greater than eq operation between a[i] and a[i+1]
             if a[i] >= a[i+1]:
                 i=i+1
                 continue 
             else : 
                 temp = a[i] 
                 a[i] = a[i+1] 
                 a[i+1] = temp 
          i=i+1
          print i
      return arr 

if __name__ == "__main__":
    a = [16,13,89,3,3]
    print returnWiggled(a)
