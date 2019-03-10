#fibonacci, factorial ve power fonksiyonlarında da recursive ve loop seçenekleri

#Loop Fibonacci

def fibonacci_loop(n):
  a,b=0,1
  for i in range(n-1):
    a,b=b,a+b
  return a
result=fibonacci_loop(5)
print(result)

#----------------------------------------------------

#Recursive Fibonacci

def fibonacci_recursive(n):
  if(n<=3):
    return 1
  else:
    return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

result=fibonacci_recursive(7)
print(result)

#----------------------------------------------------

#Recursive Factorial

def factorial_recursive(n):
  if(n==1):
    return 1
  else:
    return n*factorial_recursive(n-1)

result=factorial_recursive(4)
print(result)

#----------------------------------------------------

 #Loop Factorial

def factorial_loop(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

result=factorial_loop(6)
print(result)

#----------------------------------------------------

#Loop Power

def power_loop(m,n):
  s=1
  for i in range(n):
    s=s*m
  return s

result=power_loop(3,4)
print(result)

#----------------------------------------------------

#Recursive Power

def power_recursive(m,n):
  if(n==0):
    return 1
  elif(n==1):
    return m
  elif(n%2==0):
    return power_recursive(m*m,n//2)
  elif(n%2!=0):
    return power_recursive(m*m,n//2)*m

result=power_recursive(4,5)
print(result)

#----------------------------------------------------

#denemeler
'''for i in range(2,10):
    r_1,r_2=power_loop(i,i),power_recursive(i,i)
    print("power loop :",r_1,end=" ")
    print("power recursive:",r_2)

for i in range(20):
    r_1,r_2=fibonacci_loop(i),fibonacci_recursive(i)
    print("fibo loop :",r_1,end=" ")
    print("fibo recursive:",r_2)


for i in range(10,20):
    r_1,r_2=factorial_loop(i),factorial_recursive(i)
    print("factorial loop :",r_1,end=" ")
    print("factorial recursive:",r_2)'''
