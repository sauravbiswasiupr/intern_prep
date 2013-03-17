#!/usr/bin/python

def binary_search(arr,num):
  
   n = len(arr) 
   low  = 0 
   high = n-1 
   found = False 
   mid=(low+high)//2  
   
   while(low<=high):
       if arr[mid] == num:
         found = True 
         index = mid
         return index,found 
         
       if  num < arr[mid]:
           
           high=mid-1 
           mid = (low+high)//2
       if num > arr[mid]:
           
           low =mid+1 
           mid = (low+high)//2 
   return None,found 

#function to find median 
def find_median(sorted_list):
    n=len(sorted_list)
    if n%2 ==0 :
       #number is even 
       num = sorted_list[(n-1)//2]+sorted_list[(n)//2]
       num   = num/2.
    if n%2 != 0:
       #number is odd
       num = sorted_list[n//2]
    return num 

if __name__ =="__main__":
  test_case=[]
  num=int(raw_input())
  dynamic_list=[]
  results=[] 
  for i in range(num):
     op,n = raw_input().split(" ")
     n = int(n)
     test_case.append((op,n))

  for tup in test_case: 
      op,n = tup 
      if op =="a" : 
       dynamic_list.append(n)
       dynamic_list.sort()
       med = find_median(dynamic_list)
       if med - int(med) != 0:
           med = str(med)
           med.rstrip('0')
           med = float(med)
           results.append(med)
       
       else:
           med = int(med)
           results.append(med)
      if op=="r":
        
        #check if number to be removed is present in the list 
        index,found =binary_search(dynamic_list,n)
        if found == False :
           med="Wrong!"
           results.append(med)
        if found == True:
           #pop the number from the dynamic_list 
           dynamic_list.pop(index)
           if len(dynamic_list)==0:
             results.append("Wrong!")
           #dont need to sort the list as it will already be sorted 
           else:
              med = find_median(dynamic_list)
              if med-int(med) != 0 :
                 med =str(med)
                 med.rstrip('0')
                 med=float(med)
                 results.append(med)
              else:
                 med = int(med)
                 results.append(med)

  for result in results:
    print result 
         
         
         
