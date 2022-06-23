p = 419
q = 443
n = p * q
 
    #Зашифрованное сообщение
c = 38656

print("Cryptotext:", c)

m1 = pow(c, (p + 1)//4, p)
#print(m1)
m2 = -pow(c, (p + 1)//4, p)
m3 = pow(c, (q + 1)//4, q)
m4 = -pow(c, (q + 1)//4, q)
 
a = q * pow(q, p-2, p)
b = p * pow(p, q-2, q)
 
M1 = (a * m1 + b * m3) % n
M2 = (a * m1 + b * m4) % n
M3 = (a * m2 + b * m3) % n
M4 = (a * m2 + b * m4) % n

#print("n=",n)
print("m1=",M1,"m2= ", M2,"m3= ", M4,"m4= ", M3)

#tests
#c = M1**2%n
#print(c)
#c = M2**2%n
#print(c)
#c = M3**2%n
#print(c)
#c = M4**2%n
#print(c)

