class PasswordHp:
    def __init__(self, password_benar, batas_percobaan=3):
        self.password_benar = password_benar
        self.batas_percobaan = batas_percobaan

    def login(self):
        while self.batas_percobaan > 0:
            try:
                password = int(input("Masukkan pass-word: "))
                
                if password == self.password_benar:
                    print("Login berhasil! Selamat datang.")
                    return
                else:
                    self.batas_percobaan -= 1
                    print("PIN salah! Sisa percobaan:", self.batas_percobaan)
            
            except ValueError:
                self.batas_percobaan -= 1
                print("PIN harus berupa angka!")
                print("Sisa percobaan:", self.batas_percobaan)
            
            finally:
                print("Percobaan diproses.\n")

        print("Akun terkunci karena terlalu banyak percobaan gagal.")


# Membuat objek dan menjalankan program
sistem = PasswordHp(2571)
sistem.login()