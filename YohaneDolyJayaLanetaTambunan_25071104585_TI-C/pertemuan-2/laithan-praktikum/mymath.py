#1. penambahan(a, b)
def tambah(a, b):
    return a + b
#2. pengurangan (a,b)
def kurang (a, b):
    return a - b
#3. perkalian (a,b)
def perkalian (a, b):
    return a * b
#4.pembagian (a,b)
def pembagian (a, b):
    return a / b
print("Pembagian tidak dapat dilakukan jika b bernilai 0")
#5.modulus (a,b)
def modulus (a, b):
    return a % b

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

output = [fibonacci (i) for i in range (5)]
print(output)

