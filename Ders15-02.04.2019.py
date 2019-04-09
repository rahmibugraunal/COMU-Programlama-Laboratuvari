#Hash to list

import random

def my_function_create(m:int,n:int) :
    
    my_list=[]
    for i in range(m):
      my_list.append([])
      for j in range(n):
        s=random.randint(-5,5)
        my_list[i].append(s)	
    return my_list 



def my_function_print(myList):
    
    m=len(myList)
    n=len(myList[0])
    for i in range(m):
      for j in range(n):
        print(myList[i][j],end=" ") 
      print()	




def my_function_convert_to_hash(myList) :
    
    my_dict={}
    
    m=len(myList)
    n=len(myList[0])
    for i in range(m):
      for j in range(n):
        my_dict[(i,j)]=myList[i][j]
    return my_dict	




def my_function_print_hash(myHashList) :
    
    print(" ")
    for key in myHashList :
      print(myHashList[key],end=" ")
	    
	



my_2d_array=my_function_create(3,2)

my_function_print(my_2d_array)

my_2d_hash=my_function_convert_to_hash(my_2d_array)

my_function_print_hash(my_2d_hash)
