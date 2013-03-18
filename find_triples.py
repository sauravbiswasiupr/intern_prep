#!/usr/bin/python 

def numDistinctTuples(a):
   n=len(a)
   triples=[]
   for i in range(n):
      maxtillnow = a[i]
      tuple_length=1
      temp_tuple=[]
      
      temp_tuple.append(a[i])
      for j in range(i+1,n):
        if a[j] > maxtillnow: 
           tuple_length = tuple_length +1
           if tuple_length > 3:

              triples.append(temp_tuple)
              break  
           temp_tuple.append(a[j])
           maxtillnow =a[j]
   return triples , len(triples)



if __name__ =="__main__":
    a=[1,1,2,2,3,4]
    triples,length= numDistinctTuples(a)
    print triples , length       
           
