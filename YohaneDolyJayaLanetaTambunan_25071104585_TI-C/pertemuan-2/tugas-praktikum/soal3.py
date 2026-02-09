def jumlah_digit(*angka):
    total=0
    for ang in angka:
        total += ang
    return total
print(jumlah_digit(1, 2, 3, 4))