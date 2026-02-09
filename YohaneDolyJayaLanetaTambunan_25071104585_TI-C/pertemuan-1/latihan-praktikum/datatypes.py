#Tipe data pada python
#Variabel dapat menyimpan data dengan tipe yang berbeda, dan tipe yang berbeda dapat melakukan hal yang berbeda pula.
#Python memiliki tipe data bawaan berikut secara default, dalam kategori-kategori ini:
#Tipe Teks: str
#Tipe Numerik: int, float, complex
#Tipe Urutan: list, tuple, range
#Tipe Pemetaan: dict
#Tipe Himpunan: set, frozenset
#Tipe Boolean: bool
#Tipe Biner: bytes, bytearray, memoryview
#Tipe None: NoneType

#str
x = str("Hello World")
print(str(x)) 
#int
x = int(20)
print(int(x)) 
#float
x = float(20.5)
print(float(x)) 
#complex
x = complex(1j)
print(complex(x)) 
#list
x = list(("apple", "banana", "cherry"))
print(list(x)) 
#tuple
x = tuple(("apple", "banana", "cherry"))
print(tuple(x))
#range
x = range (3,10)
print (list(x))
#dict
x = dict(name="John", age=36)
print(dict(x)) 
#set
x = set(("apple", "banana", "cherry"))
print(set(x)) 
#frozenset
x = frozenset(("apple", "banana", "cherry"))
print(frozenset(x)) 
#bool
x = bool(5)
print(bool(x)) 
#bytes
x = bytes(5)
print(bytes(x)) 
#bytearray
x = bytearray(5)
print(bytearray(x)) 
#memoryview
x = memoryview(bytes(5))
print(memoryview(x))
#nonetype
x = None
print(type(x)) 