def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Pembagi tidak boleh nol.")
    return a / b

def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

if __name__ == "__main__":
    print("=== UTILITAS MATEMATIKA ===")
    print("Tambah (10, 5):", tambah(10, 5))
    print("Kurang (10, 5):", kurang(10, 5))
    print("Kali (10, 5):", kali(10, 5))
    print("Bagi (10, 5):", bagi(10, 5))
    print("Luas persegi (4):", luas_persegi(4))
    print("Luas persegi panjang (5, 3):", luas_persegi_panjang(5, 3))