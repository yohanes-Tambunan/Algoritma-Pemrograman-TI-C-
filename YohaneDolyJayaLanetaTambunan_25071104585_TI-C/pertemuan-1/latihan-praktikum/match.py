#match akan memilih salah satu dari banyak blok kode untuk dieksekusi.
#Begini cara kerjanya:
#match dievaluasi sekali.
#Nilai ekspresi dibandingkan dengan nilai setiap `case`.
#Jika ada kecocokan, blok kode yang terkait akan dieksekusi.
#Contoh di bawah ini menggunakan nomor hari dalam seminggu untuk mencetak nama hari dalam seminggu
hari = 6
match hari:
  case 1:
    print("Senin")
  case 2:
    print("Selasa")
  case 3:
    print("Rabu")
  case 4:
    print("Kamis")
  case 5:
    print("Jumat")
  case 6:
    print("Sabtu")
  case 7:
    print("Minggu")