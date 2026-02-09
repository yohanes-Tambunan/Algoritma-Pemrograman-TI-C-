def rata_rata(*nilai):
    if len(nilai)== 0:
        return "Data kosong"
    rata=0
    for x in nilai:
        rata+= x
        hasil = rata/len(nilai)
    return hasil
print(rata_rata(80, 75, 90, 60, 85))
    