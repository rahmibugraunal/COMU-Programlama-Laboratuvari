import os
os.getcwd()

def get_words(my_file = "C:\\data.txt"):
    my_list = []
    f = open(my_file, "r+")
    contents = f.readlines()
    for line in contents:
        # print(line)
        words = line.split(" ")
        for word in words:
            # print(word)
            my_list.append(word)
    # print(contents)
    f.close()
    return my_list

def get_hist(my_list):
    my_hist = {}
    for w in my_list:
        if w in my_hist.keys():
            my_hist[w] = my_hist[w]+1
        else:
            my_hist[w] = 1
    return my_hist

def get_files(path_1):
    file_s = [file for file in my_list if os.path.isfile(file)]
    return file_s

lst_1 = get_words()
get_hist(lst_1)

my_list=os.listdir()

for item in my_list:
    if os.path.isdir(item):
        print(item)
    if os.path.isfile(item):
        print(item)

dir_s = [dir for dir in my_list if os.path.isdir(dir)]
file_s = [file for file in my_list if os.path.isfile(file)]

from sympy import Symbol
import math
theta=Symbol('theta')
u=Symbol('u')
t=Symbol('t')
g=Symbol('g')

theta=Symbol('theta')

x=Symbol('x')

from sympy import Limit,S

l=Limit(1/x,x,S,dir='-')    
print(l)

t=Symbol('t')
t1=Symbol('t1')
delta_t=Symbol('delta_t')

st=5*t**2+2*t+8

st1=st.subs({t:t1})

st1_delta=(st.subs({t:t+delta_t}))

f_d=Limit((st1_delta-st1)/delta_t),0)

print(f_d)
