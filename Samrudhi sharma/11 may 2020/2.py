arr = []
n = input("enter the range:")

for i in range(n):
	arr.append(i)

ele = 0
for i in range (n):
	ele = arr[i]^arr[i+1]

if (ele == 0):
	print("Yes")

else:
	print("No")
