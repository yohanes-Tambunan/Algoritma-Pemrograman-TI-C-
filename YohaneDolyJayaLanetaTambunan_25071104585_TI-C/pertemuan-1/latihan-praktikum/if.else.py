#1. kondisi dan pernyataan if python
#Python mendukung kondisi logika umum dari matematika:
#Sama dengan: a == b
#Tidak sama dengan: a != b
#Kurang dari: a < b
#Kurang dari atau sama dengan: a <= b
#Lebih besar dari: a > b
#Lebih besar dari atau sama dengan: a >= b
#Kondisi ini dapat digunakan dalam beberapa cara, yang paling umum dalam "pernyataan if" dan perulangan.

#contoh
a = 33
b = 54
if b > a:
  print("b lebih besar dari a")

#2. elif
#elif adalah cara Python untuk mengatakan "jika kondisi sebelumnya tidak benar, maka coba kondisi ini".
#Kata kunci elif memungkinkan Anda untuk memeriksa beberapa ekspresi untuk nilai True dan mengeksekusi blok kode segera setelah salah satu kondisi bernilai True.

#contoh
a = 33
b = 33
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b adalah sama")

#3. else
#Kata kunci `else` menangkap apa pun yang tidak ditangkap oleh kondisi sebelumnya.

#contoh
a = 53
b = 30
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b adalah sama")
else:
  print("a lebih besar dari b")

#4. shorthand if
#Jika kita hanya memiliki satu pernyataan untuk dieksekusi, Anda dapat meletakkannya pada baris yang sama dengan pernyataan if.

#contoh
a = 7
b = 5
if a > b: print("a lebih besar dari b")

#5. Python Logical Operators
#Operator logika digunakan untuk menggabungkan pernyataan kondisional. Python memiliki tiga operator logika

#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("kedua kondisi sama")

#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("setidaknya satu dari kedua kondisi tersebut benar")

#not
a = 43
b = 100
if not a > b:
  print("a tidak lebih besar dari b")

#6. Nested If Statements
#kita dapat memiliki pernyataan if di dalam pernyataan if lainnya. 

#contoh
score =80
attendance = 80
submitted = True

if score >= 60:
  if attendance >= 70:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#7. The pass statement
#Pernyataan `pass` berguna dalam beberapa situasi:
#Saat Anda membuat struktur kode tetapi belum mengimplementasikan logikanya
#Saat sebuah pernyataan diperlukan secara sintaksis tetapi tidak diperlukan tindakan apa pun
#Sebagai tempat penampung untuk kode di masa mendatang selama pengembangan
#Dalam fungsi atau kelas kosong yang Anda rencanakan untuk diimplementasikan nanti

#contoh
nilai = 16

if nilai < 18:
  pass # TODO: 
else:
  print("bagus")
  