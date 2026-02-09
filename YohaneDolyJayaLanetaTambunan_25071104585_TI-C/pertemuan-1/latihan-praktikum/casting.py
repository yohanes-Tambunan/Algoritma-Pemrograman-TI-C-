#casting (konversi tipe) adalah proses mengubah nilai dari satu tipe data ke tipe data lain. 
# Hal ini dilakukan menggunakan fungsi bawaan yang sesuai dengan tipe yang diinginkan, seperti int(), float(), dan str()
#python menyediakan beberapa fungsi bawaan untuk konversi tipe data secara eksplisit
#int(x): Mengonversi x menjadi bilangan bulat. Jika x berupa bilangan pecahan (float), bagian desimalnya dihilangkan (dipotong), dan jika berupa string, maka harus berupa bilangan bulat.
#float(x): Mengonversi x menjadi bilangan floating-point. Menerima bilangan bulat, bilangan floating-point, atau string yang mewakili angka yang valid.
#str(x): Mengonversi x menjadi representasi string. Fungsi ini bekerja pada berbagai macam tipe data.

#int
x = int (1) #x akan menjadi 1
y = int (2.8) #y akan menjadi 2
z = int ("3") # z will be 3
print(x)
print(y)
print(z)

#float
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print (w)

#string
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x)
print(y)
print(z)