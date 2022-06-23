q = 9
p = 23
nA = 4
nB = 3

Ya = (q ** nA) % p
Yb = (q ** nB) % p

Ka = (Yb ** nA) % p
Kb = (Ya ** nB) % p

print("Ya = ", Ya)
print("Yb = ", Yb)

if Ka == Kb:
	print("K = ", Ka)
else:
	print("Something went wrong")