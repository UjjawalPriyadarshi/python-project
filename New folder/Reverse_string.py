def reverse(s):
	str = " "
	for i in s:
		str = i + str
	return str

s = "Hello World"

print("The original string is :",end = " ")
print(s)

print("The reverse string is :",end = " ")
print( reverse(s))