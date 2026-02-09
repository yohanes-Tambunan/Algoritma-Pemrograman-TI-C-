#The while loops
#Dengan while loops, kita dapat mengeksekusi serangkaian pernyataan selama suatu kondisi benar.

#contoh
i = 1
while i < 6:
  print(i)
  i += 1

#the break statement
#kita dapat menghentikan loops meskipun kondisi while benar

#contoh
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#the continue statement
#kita dapat menghentikan iterasi saat ini dan melanjutkan ke iterasi berikutnya

#contoh
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#the else statement
#kita dapat menjalankan blok kode sekali saja ketika kondisi tersebut tidak lagi benar

#contoh
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")