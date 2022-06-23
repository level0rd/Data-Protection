pA = 127
pB = 89

gA = 7
gB = 7

xA = 63
xB = 44

kA = 25
kB = 17

M = 31

#a,b from 5)
incA = 118
incB = 105


#1
yA = gA ** xA % pA
yB = gB ** xB % pB
print("1)")
print("yA =", yA,"yB =", yB)

#2
print("2)")
print("{pA = %d, gA = %d, yA = %d}"%(pA,gA,yA))

#3
print("3)")
print("{pB = %d, gB = %d, yB = %d}"%(pB,gB,yB))

#4
#to send data to B from A we use keys B sent us earlier such as gB,pB,yB, however, we still use kA

aA = gB ** kA % pB #здесь может быть ошибка, я не уверен, чье g мы используем #ps здесь только kA свой
bA = M * yB ** kA % pB
print("4)")
print("aA = %d, bA = %d"%(aA,bA))

#5
#Decryption gA,pA,yA  incA incB are available 
incM = incB*(incA ** (pA - 1 - xA)) % pA 
print("5)")
print("M from B= ", incM)