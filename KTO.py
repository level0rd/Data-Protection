#Task 1
print("--------TASK1--------")
a=28
b=1149
m=31

fi=m-1
powerFi=b % fi

answer = a ** powerFi % m

print("fi = %d; power mod fi=%d, answer=%d"%(fi,powerFi,answer))

#Task 2
#остатки
print("--------TASK2--------")
b1=4
b2=6
b3=12

#модули
m1=67
m2=17
m3=31

M=m1*m2*m3

print("M=",M)

#Находим N
n1=M//m1
n2=M//m2
n3=M//m3

#This works _
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#Находим инверс ni
x1 = modinv(n1,m1)
x2 = modinv(n2,m2)
x3 = modinv(n3,m3)

print("x1=",x1)
print("x2=",x2)
print("x3=",x3)

bnx1=b1*n1*x1
bnx2=b2*n2*x2
bnx3=b3*n3*x3

print("bnxi: ", bnx1,bnx2,bnx3)
#checks
check1=bnx1%m1
check2=bnx2%m2
check3=bnx3%m3

#print("Предпроверки(bnxi/modI): ",check1,check2,check3)
#print("Настоящие остатки): ",b1,b2,b3) Переформатируйте, если тоже хотите добавить их в ответ

X=bnx1+bnx2+bnx3
answ=X%M
print("bnx sum:",X)
print("x=",answ)