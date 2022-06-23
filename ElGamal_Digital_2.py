#Проверка подписи
y = 695
g = 660
p = 2617
m = 88
a = 660
b = 1540

left = (y**a)*(a**b)%p
right = (g**m)%p
if  left == right:
    print("Подпись верна")
else:
    print("Подпись неверна")
print("Левая часть:", left)
print("Правая часть:", right)