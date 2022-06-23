from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    i = 1
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n,a):
        p = prod / n_i
        i += 1
        sum += a_i* mul_inv(p, n_i) * p
    return sum % prod
def mul_inv(a, b):
    b0 = b
    x0, x1= 0,1
    i = 0
    if b == 1: 
    	return 1
    while a>1 :
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: 
    	x1 += b0
    i += 1
    return x1



p = 2339
q = 1709
m = 1142599
e = 3

n = p * q
f = (p-1)*(q-1)


d = mul_inv(e, f)
#print ('Open key: {%s,%s}' % (e,n))
#print ('Secret key: {%s,%s}' % (d,n))
c1 = 1

for i in range(e):
	c1 *= m
c = c1 % n
print("Open text:", m)
print('Encrypted text = ', c)

a=[p,q]
r=[((c % p)**(d%(p-1)))%p,((c%q)**(d%(q-1)))%q]

r1 = ((c % p)**(d%(p-1)))%p
r2 = ((c%q)**(d%(q-1)))%q

print("p=",p,"q=",q,"n=",n,"fi:",f,"e=",e,"d=",d)
print("crypto mod(p)",c % p)
print("crypto mod(q)",c % q)
print("d mod(p-1)=",d%(p-1))
print("d mod(q-1)=",d%(q-1))
print("c^dmodp=",r1)
print("c^dmodq=",r2)
print("a=",a)
print("r=",r1,r2)
print()
print ('Decryption result: ',chinese_remainder(a,r)," mod=",n)