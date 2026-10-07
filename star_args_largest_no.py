def x (*num):
	largest=num[0]
	for n in num:
		if n>largest:
			largest=n
	print("largest number:",largest)
x(90,89,56,23,41,100)
			