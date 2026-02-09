#variabel adalah tempat menyimpan data 
#penjelasan variabel terbagi atas beberapa sub-bab


#1. variabel pada python
#python adalah nama simbolik untuk wadah penyimpanan data yang tidak memiliki perintah untuk mendeklarikan variabel, hanya dengan menetapkan nilai menggunakan data

#cara menaruh/assigmnent nilai
a = 10
b = 20
c = 30
#pemanggil
print("Nilai a = ", a)
print("Nilai b = ", b)
print("Nilai c=  ", c)

#2. aturan penamaan pada variabel
#adapun aturannya yaitu 
#Nama variabel harus diawali dengan huruf atau karakter garis bawah
#Nama variabel tidak boleh diawali dengan angka
#Nama variabel hanya boleh berisi karakter alfanumerik dan garis bawah (A-z, 0-9, dan _)
#Nama variabel peka terhadap huruf besar dan kecil (usia, Age, dan AGE adalah tiga variabel yang berbeda)
#Nama variabel tidak boleh berupa kata kunci Python.

#contoh penaamaan yang benar
nilai_y= 100 #dengan menngunakan underscore
jumlah10= "Yohanes" #angka tidak boleh didepan
nilaifais= 20 #tanpa spasi

#3. penetapan beberapa nilai 

#dalam python kita dapat menetapkan beberapa nilai ke beberapa variabel berbeda dalam satu baris menggunakan koma. 
#Jumlah variabel harus sesuai dengan jumlah nilai. 
k, l, m, n, o, p = "Sapi", "Kerbau", "Jerapah", "Koala", "Domba", "Anoa"
#pemanggil
print (k)
print (l)
print (m)
print (n)
print (o)
print (p)

#dalam python kita dapat menetapkan satu nilai ke beberapa variabel secara bersamaan dengan menggunakan tanda sama dengan 
x = y = z = "Jus jambu"
print (x)
print (y)
print (z)

#4 output pada variabel
#pada python untuk menampilkan variabel sering menggunakan fungsi print()
d = "kamu keren"
print (d)
#ketika ingin menggabungkan variabel satu dengan variabel lain, selalu dihubungkan dengan koma.
e = "5"
f = "nilai kamu"
print (x, y)

#5 variabel global
#Variabel global dapat digunakan oleh siapa saja, baik di dalam fungsi maupun di luar fungsi.
g = "bagus"
def myfunc():
    print("nilai kamu " + g)
myfunc()

 
