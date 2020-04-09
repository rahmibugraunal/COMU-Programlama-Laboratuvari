#pow fonksiyonu
def power(a,b):
    if b==0:
           return 1
    elif b==1:
           return a
    else:
            #return a*power(a,b-1)    
           #return power(a*a,b/2)     
#recursive pow fonksiyonu
          if b%2==0:
              return power(a*a,b//2)
          else:
              return power(a*a,b//2)*a

print(pow(3,4))   #3'un 4.kuvveti=81

#Toplami en büyük olan alt kumeyi bulma
liste_1=[4,-3,5,-2,-1,2,6,-2]
max=0
for i in range(8):
    for j in range(i,8):
        t=0
        for k in range(i,j):
            t=t+liste_1[k]
        if max<t:
            max=t
            i_1,i_2=i,j
print(max,i_1,i_2)   #(11,0,7)



#bubble sort
def bubbleSort(list_1):
  n= len(list_1)

  for i in range (n,0,-1):
  
    for j in range(n):

      if list_1[j]> list_1[j+1]:
        t = list_1[j+1]
        list_1[j+1]=list_1[j]
        list_1[j] =t
        
return list_1

#selection sort
def selectionSort(list_1):
  n = len(list_1)

  for i in range(n): 
       
    min = i 
    for j in range(i+1, n): 
        if A[min] > A[j]: 
            min = j 
               
    A[i], A[min] = A[min], A[i] 
  
return list_1
