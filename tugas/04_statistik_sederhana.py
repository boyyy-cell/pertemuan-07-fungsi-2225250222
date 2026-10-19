def hitung_statistik(data):
    if not data:
        return None

    return {
        "jumlah": sum(data),
        "rata_rata": sum(data) / len(data),
        "minimum": min(data),
        "maksimum": max(data),
    }

angka = input("Masukkan beberapa angka, pisahkan dengan spasi: ")
data = [float(x) for x in angka.split()]

hasil = hitung_statistik(data)

if hasil:
    print(f"Jumlah: {hasil['jumlah']}")
    print(f"Rata-rata: {hasil['rata_rata']:.2f}")
    print(f"Nilai minimum: {hasil['minimum']}")
    print(f"Nilai maksimum: {hasil['maksimum']}")
else:
    print("Data tidak boleh kosong.")