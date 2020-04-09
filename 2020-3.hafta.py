def my_h(list_1):
    my_d={}
    for item in list_1:
        if item not in my_d:
            my_d[item]=1
        else:
            my_d[item]=item+1
    return my_d
print(my_h([2,3,4,6,2,5,6,6,6,6,6,6,6,2]))

#{2: 3, 3: 1, 4: 1, 5: 1, 6: 7}

def lookup(d,V):
    for key in d:
        if d[key]==V:
            return key
    return -1

my_d =dict()
my_d ={1:3,2:5,6:8}
print(lookup(my_d,5))

#recurcive fibonnacci
known={0:0,1:1}
def fibo_rec(n):
  # if n<2:
       #return n
   #else:
        #return fibo_rec(n-1)+fibo_rec(n-2)
    
#Zar için olasilik hesabi 
from sympy import FiniteSet

t = FiniteSet(1,2,3)
s = FiniteSet(2,4,6)

t==s
t.union(s)
t.intersect(s)

t**2

#olasilik hesaplama
def probability(space, event):
  return len(event)/len(space)

#asal mi 
def check_prime(number):
  if number!=1:
    for factor in range(2,number):
      if number % factor == 0:
        return False
  else:
    return False
  return True

space = FiniteSet(*range(1,21))
primes=[]
for num in space:
  if check_prime(num):
    primes.append(num)

event = FiniteSet(*primes)
p = probability(space, event)
print(p)    
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1)+fibo_rec(n-2)
        known[n]=result
        #print(known)
        return result
print(fibo_rec(10))
