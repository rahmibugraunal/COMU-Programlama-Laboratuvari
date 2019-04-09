# Bozuk parayla verilecek para üstünü en az sayıda bozuk para ile veren fonksiyon

def coin(n):

    coinlist=[1,5,10,25,50,100]
    b=[]
    c=[]
    a=n
    z=len(coinlist)-1
    while(a!=0):
        for i in range(z,-1,-1):
            if(a>=coinlist[i]):
                while(a>=coinlist[i]):
                    a=a-coinlist[i]
                    b.append(coinlist[i])
    a = n
    z = len(coinlist) - 1
    while(a!=0):
        for j in range(z,-1,-1):
            if(a%coinlist[j]==0):
                while(a!=0):
                    a=a-coinlist[j]
                    c.append(coinlist[j])
    if(len(b)<len(c)):
        return b
    else:
        return c

x=int(input("Para ustunu giriniz: "))
print("Verilecek bozuk paralar: ",coin(x))
