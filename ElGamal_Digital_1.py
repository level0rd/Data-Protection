#Составление цифровой подписи
y= 260 
g= 2785
p= 3221 
x= 2502 
k= 1611 
m= 1711

def modInverse(a,m):         
    for x in range(1,m):
        if (((a%m) * (x%m)) % m == 1):
           return x
    return 1
    pass

#k_1 = (libnum.invmod(k, p-1)) 
k_1 = modInverse(k, p-1)
a = (g ** k) % p 
print ('a = ', a)

b = (m-x*a)*k_1  % (p-1)
print ('b = ', b)

