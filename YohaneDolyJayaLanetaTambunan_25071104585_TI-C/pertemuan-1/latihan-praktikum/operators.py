#1. Operator Aritmatika
#Operator aritmatika digunakan dengan nilai numerik untuk melakukan operasi matematika umum.
#Penjumlahan
x = 5
y = 10

print(x + y)

#Pengurangan
x = 10
y =5

print(x - y)

#pembagian
x = 6
y = 3

print (x/y)

#perkalian
x = 7
y = 2

print (x * y)

#pengembalian sisa dari operasi pembagian
x = 6
y = 4

print (x % y)

#perpangkatan
x = 3
y = 5

print(x ** y) #sama dengan 3*3*3*3*3


#membulatkan hasil kebawah dari bilangan bulat terdekat
x = 15
y = 2

print(x // y)

#2.Operator Penugasan
#Operator penugasan digunakan untuk menetapkan nilai ke variabel.
#=
x = 4
print(x)

#+=
x = 4
x += 3
print(x)

#-=
x = 4
x -= 3
print(x)

#*=
x = 5
x *= 3
print(x)

#/=
x = 5
x /+= 1
print(x)

#%=
x = 5
x %= 3
print(x)

#//=
x = 7
x //= 3
print(x)

#**=
x = 8
x **= 3
print(x)

#&=
x = 5
x &= 3
print(x)

#|= 
x = 5
x |= 3
print(x)

#^=
x = 5
x ^= 3
print(x)

#>>=
x = 5
x >>= 3
print(x)

#<<=
x = 5
x <<= 3
print(x)

#:=
print(x:=3)

#3. Operator Perbandingan
#Operator perbandingan digunakan untuk membandingkan dua nilai
#sama dengan
x = 5
y = 3
print(x == y)# bernilai salah dikarenakan 5 tidak sama dengan 3

#Tidak sama dengan
x = 5
y = 3

print(x != y)#bernilai benar karena 5 tidak sama dengan 3

#lebih besar dari 
x = 7
y = 6

print(x > y)#bernilai benar dikarenakan 7 lebih besar dari 6

#lebih kecil dari
x = 7
y = 6

print(x < y)#bernilai salah dikarenakan 6 tidak lebih besar dari 7

#lebih besar dari atau sama dengan
x = 10
y = 7

print(x >= y)#bernilai benar dikarenakan 10 lebih besar dari atau sama dengan 7

#lebih kecil dari atau sama dengan
x = 10
y = 7

print(x <= y)#bernilai salah dikarenakan 7 tidak lebih besar dari atau sama dengan 10

#4. Operator Logika
#Operator logika digunakan untuk menggabungkan pernyataan bersyarat:

#and
#Mengembalikan True jika kedua pernyataan benar
x = 7

print(x > 4 and x < 12)

#or 
#Mengembalikan True jika salah satu pernyataan benar 
x = 7

print(x > 2 or x < 3)#bernilai benar karena satu diantara kondisi tersebut benar

#not
#mengembalikan False jika hasilnya benar 
x = 8

print(not(x > 2 and x < 10))

#5. Operator Identitas
#Operator identitas digunakan untuk membandingkan objek, bukan apakah keduanya sama, tetapi apakah keduanya benar-benar objek yang sama, dengan lokasi memori yang sama
#is
#bernilai True jika kedua variabel adalah objek yang sama
x = ["apel", "pisang"]
y = ["apel", "pisang"]
z = x

print(x is z)
#mengembalikan nilai True dikarenakan z sama dengan x
print(x is y)
# mengembalikan nilai False dikarenakan x tidak sama dengan y, bahkan jika mereka mempunya kata yang sama 
print(x == y)
#untuk mengembalikan nilai True pada x dan y menggunakan ==

#is not
#Mengembalikan True jika kedua variabel bukan objek yang sama
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# bernilai False dikarenakan z sama dengan x 
print(x is not y)
# bernilai True dikarenakan x tidak sama dengan y 
print(x != y)
#untuk mengembalikan nilai False menggunakan !=

#6. Operator keanggotaan
#Operator keanggotaan digunakan untuk menguji apakah suatu urutan ada dalam suatu objek
#in 
#Mengembalikan True jika suatu urutan dengan nilai yang ditentukan ada dalam objek
sayur = ["tomat", "bayam", "timun"]
print=("bayam" in sayur)

#not in
#Mengembalikan True jika suatu urutan dengan nilai yang ditentukan tidak ada dalam objek
sayur = ["tomat', "bayam", "timun"]
print=("kangkung" not in sayur)

#7.Operator Bitwise
#Operator bitwise adalah operator yang bekerja langsung pada bit (biner: 0 dan 1) dari sebuah bilangan.Angka yang kita pakai sehari-hari (desimal) akan diubah komputer jadi biner (bit).
#AND &
#Mengatur setiap bit menjadi 1 jika kedua bit =1
print(6 & 3)

#OR |
#mengatur 1 jika salah satu 1
print(5 | 3)

#XOR ^
#1 jika bit berbeda
print (5 ^ 3)

#NOT ~
#membalik semua bit
print(~5)

#Left Shift <<
#Geser bit ke kiri
print (5<<1)

#Right Shift >>
#Geser bit ke kanan 
print (5>>1)

#7. Urutan Prioritas
#Urutan prioritas dijelaskan di bawah ini, dimulai dengan prioritas tertinggi di bagian atas

#1	( )	Tanda kurung
#2	+ - ~	Unary (positif, negatif, NOT bitwise)
#3	* / // %	Aritmatika
#4	+ -	Penjumlahan & pengurangan
#5	<< >>	Bit shift
#6	&	Bitwise AND
#7	^	Bitwise XOR
#8	`	`
#9	< > <= >=	Perbandingan
#10	== !=	Persamaan
#11	not	Logika NOT
#12	and	Logika AND
#13	or	Logika OR
#14	= += -= *= /=	Assignment