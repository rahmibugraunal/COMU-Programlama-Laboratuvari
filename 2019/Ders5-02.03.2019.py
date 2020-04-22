#Vektör işlemleri

#Vektörel Çarpım
def MyVektorInnorProduct(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*w[i]
    t=0
    for i in range (size):
        t=t+my_result[i]
    return t

#-------------------------------------------

#Skaler Çarpım
def MyVektorScalarProduct(alpha,v):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=alpha*v[i]
    return my_result

#-------------------------------------------

#Çıkarma
def MyVektorSubtraction(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]-w[i]
    return my_result

#-------------------------------------------

#Toplama
def MyVektorAddition(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]+w[i]
    return my_result
