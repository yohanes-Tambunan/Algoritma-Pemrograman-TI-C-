#1. string dalam python
#string dalam python dikelilingi oleh tanda kutip tunggal atau ganda
#string adalah karakter yang digunakan untuk menangani data tekstual
#kita dapat menampilkan string dengan fungsi print()

#contoh
print ("salam ")
print ('salam')

#Anda dapat menetapkan string multibaris ke variabel dengan menggunakan tiga tanda kutip
#contoh
a = """saya suka bermain catur,
saya suka bermain bola,
saya suka belajar teknik informatika."""
print (a) 

#2.String Slicing?
#Slicing adalah cara mengambil sebagian karakter dari sebuah string (teks) di Python.
#contoh
b = "Hello, World!"
print(b[2:5])
#String "Hello, World!" memiliki indeks mulai dari 0
#maka output nya akan menjadi llo 
#mulai dari 2-5 (sebelum 5) 

#3. modifikasi string
#python memiliki serangkaian metode bawaan yang dapat kita gunakan pada string.
#contoh
a = "kamu keren!"
print(a.upper())

a = "kamu keren!"
print(a.lower())

#bisa juga menghapus spasi kosong 
a = " kamu keren! "
print(a.strip()) 

#4.menggabungkan string
#untuk menggabungkan, atau menyatukan, dua string, kita dapat menggunakan operator +
#contoh
a = "kamu"
b = "keren"
c = a + " " + b
print(c)
#untuk menambahkan spasi diantara dua kata tersebut,tambahkan simbol " "

#5. format pada string
#kita bisa menggabungkan strings dan angka dengan menambahkan huruf f, dan simbol {}
#contoh
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#6. escape pada string
#Untuk menyisipkan karakter yang tidak diizinkan dalam sebuah string, gunakan karakter escape.
#Karakter escape adalah garis miring terbalik \ diikuti oleh karakter yang ingin Anda sisipkan.
#contoh
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
 
#escape karakter lain yang digunakan dalam python
#single quote
txt = 'It\'s wrong.'
print(txt) 

#backslach
txt = "This will insert one \\ (backslash)."
print(txt) 

#New line
txt = "Hello world\nhello!"
print(txt) 

#carriage return
txt = "kamu\rkeren"
print(txt) 

#Tab
txt = "kamu\tkeren!"
print(txt) 

#backspace
txt = "kamu \bkeren!"
print(txt) 

#7.Metode String
#Python memiliki serangkaian metode bawaan yang dapat digunakan pada string.
#capitalize()	Mengubah huruf pertama menjadi huruf besar
#casefold()	Mengubah seluruh string menjadi huruf kecil
#center()	Mengembalikan string yang diposisikan di tengah
#count()	Menghitung jumlah kemunculan nilai tertentu dalam string
#encode()	Mengembalikan versi string yang telah dienkode
#endswith()	Mengembalikan True jika string diakhiri dengan nilai tertentu
#expandtabs()	Mengatur ukuran tab pada string
#find()	Mencari nilai tertentu dalam string dan mengembalikan posisi ditemukannya
#format()	Memformat nilai tertentu ke dalam string
#format_map()	Memformat nilai tertentu ke dalam string
#index()	Mencari nilai tertentu dalam string dan mengembalikan posisi ditemukannya
#isalnum()	Mengembalikan True jika semua karakter adalah alfanumerik
#isalpha()	Mengembalikan True jika semua karakter berupa huruf
#isascii()	Mengembalikan True jika semua karakter adalah karakter ASCII
#isdecimal()	Mengembalikan True jika semua karakter berupa bilangan desimal
#isdigit()	Mengembalikan True jika semua karakter berupa digit
#isidentifier()	Mengembalikan True jika string merupakan identifier
#islower()	Mengembalikan True jika semua karakter adalah huruf kecil
#isnumeric()	Mengembalikan True jika semua karakter berupa angka
#isprintable()	Mengembalikan True jika semua karakter dapat dicetak
#isspace()	Mengembalikan True jika semua karakter berupa spasi
#istitle()	Mengembalikan True jika string mengikuti aturan judul
#isupper()	Mengembalikan True jika semua karakter adalah huruf besar
#join()	Menggabungkan elemen iterable ke dalam string
#ljust()	Mengembalikan string dengan rata kiri
#lower()	Mengubah string menjadi huruf kecil
#lstrip()	Menghapus spasi di sebelah kiri string
#maketrans()	Membuat tabel translasi untuk digunakan dalam penerjemahan
#partition()	Membagi string menjadi tiga bagian dalam bentuk tuple
#replace()	Mengembalikan string dengan nilai tertentu diganti nilai lain
#rfind()	Mencari nilai tertentu dan mengembalikan posisi terakhir ditemukannya
#rindex()	Mencari nilai tertentu dan mengembalikan posisi terakhir ditemukannya
#rjust()	Mengembalikan string dengan rata kanan
#rpartition()	Membagi string menjadi tiga bagian dalam bentuk tuple dari kanan
#rsplit()	Memisahkan string berdasarkan pemisah tertentu dari kanan
#rstrip()	Menghapus spasi di sebelah kanan string
#split()	Memisahkan string berdasarkan pemisah tertentu
#plitlines()	Memisahkan string berdasarkan baris
#startswith()	Mengembalikan True jika string diawali nilai tertentu
#swapcase()	Menukar huruf kecil menjadi besar dan sebaliknya
#title()	Mengubah huruf pertama setiap kata menjadi huruf besar
#translate()	Mengembalikan string yang telah diterjemahkan
#upper()	Mengubah string menjadi huruf besar
#zfill()	Mengisi string dengan angka 0 di bagian depan sesuai jumlah tertentu