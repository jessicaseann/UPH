import random

a = []
for i in range (100) :
	a.append(random.randint(1,100))

print("List of numbers: ")
for i in range (100) :
	print(str(a[i]),end = ' ')
print()

a.sort()
print("Number in ascending order: ")
for i in range (100) :
	print(str(a[i]),end = ' ')
print()

b = sorted(a, reverse=True)
print("Number in descending order: ")
for i in range (100) :
	print(str(b[i]),end = ' ')
print()

