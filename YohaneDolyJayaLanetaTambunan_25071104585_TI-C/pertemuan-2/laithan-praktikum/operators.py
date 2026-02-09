#Operator aritmatika
#Operator	Name	Example	Try it
#+	Addition	x + y	
#-	Subtraction	x - y	
#*	Multiplication	x * y	
#/	Division	x / y	
#%	Modulus	x % y	
#**	Exponentiation	x ** y	
#//	Floor division	x // y

#contoh
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 12
y = 5

print(x / y)

x = 12
y = 5

print(x // y)

#Operator penugasan
#Operator	Example	Same As	Try it
#=	x = 5	x = 5	
#+=	x += 3	x = x + 3	
#-=	x -= 3	x = x - 3	
#*=	x *= 3	x = x * 3	
#/=	x /= 3	x = x / 3	
#%=	x %= 3	x = x % 3	
#//=	x //= 3	x = x // 3	
#**=	x **= 3	x = x ** 3	
#&=	x &= 3	x = x & 3	
#|=	x |= 3	x = x | 3	
#^=	x ^= 3	x = x ^ 3	
#>>=	x >>= 3	x = x >> 3	
#<<=	x <<= 3	x = x << 3	
#:=	print(x := 3)	x = 3 print(x)	

#Operator perbandingan
#Operator	Name	Example	Try it
#==	Equal	x == y	
#!=	Not equal	x != y	
#>	Greater than	x > y	
#<	Less than	x < y	
#>=	Greater than or equal to	x >= y	
#

#contoh
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5

print(1 < x < 10)

print(1 < x and x < 10)

#operator logika
#Operator	Description	Example	Try it
#and 	Returns True if both statements are true	x < 5 and  x < 10	
#or	Returns True if one of the statements is true	x < 5 or x < 4	
#not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

#contoh
x = 5

print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x > 3 and x < 10))

#operator identitas
#Operator	Description	Example	Try it
#is 	Returns True if both variables are the same object	x is y	
#is not	Returns True if both variables are not the same object	x is not y

#contoh
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#operasi keanggotaan
#Operator	Description	Example	Try it
#in 	Returns True if a sequence with the specified value is present in the object	x in y	
#not in	Returns True if a sequence with the specified value is not present in the object	x not in y	

#contoh
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#operator bitwise
#Operator Name	Description	Example	Try it
#& 	AND	Sets each bit to 1 if both bits are 1	x & y	
#|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
#^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
#~	NOT	Inverts all the bits	~x	
#<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
#>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

#contoh
print(6 & 3)

#operator presedence
#contoh

print((6 + 3) - (6 + 3))


