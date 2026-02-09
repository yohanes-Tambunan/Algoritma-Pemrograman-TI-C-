def hitung_prima(n):
    if n <= 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


hasil = [i for i in range(1, 51) if hitung_prima(i)]
print(hasil)
