def my_f_1(list_1=[-4, -3, 5, -2, -1, 2, 6, -2]):

    n=len(list_1)
    maxSum=0
    for i in range(n):
        for j in range(i+1,n):
            print(i,j)
            t=0
            for k in range(i,j+1):
                t=t+list_1[k]
            if(t>maxSum):
                maxSum=t
    return maxSum

def my_f_2(list_1=[-4, -3, 5, -2, -1, 2, 6, -2]):

    n= len(list_1)
    maxSum=0
    for i in range(n):
        t=0
        for j in range(i,n):
                t=t+list_1[j]
                if(t>maxSum):
                  maxSum = t
    return maxSum
#iki sayidan max olani donduren fonksiyon 
def max_of_two(a,b):
  if a>b:
    return a
  else:
    return b  
#uc sayidan max olani donduren fonksiyon
def max_of_three(a,b,c):
  return max_of_two(a,max_of_two(b,c))    

def my_f_3(list_1=[-4, -3, 5, -2, -1, 2, 6, -2]):
    n = len(list_1)
    if (n==1):
        return list_1[0]
    left_i = 0
    left_j = n//2
    right_i = n//2
    right_j = n
    left_sum = my_f_3(list_1[left_i:left_j])
    right_sum = my_f_3(list_1[right_i:right_j])

    temp_left_sum = 0
    t = 0

    for i in range(left_j-1, left_i-1, -1):
        t = t + list_1
        if(t > temp_left_sum):
            temp_left_sum = t
    temp_right_sum = 0
    t = 0

    for i in range(right_i, right_j):
        t = t + list_1[i]
        if (t > temp_right_sum):
            temp_right_sum = t
    center_sum = temp_left_sum + temp_right_sum

    return max_of_three(temp_left_sum,temp_right_sum,center_sum)
