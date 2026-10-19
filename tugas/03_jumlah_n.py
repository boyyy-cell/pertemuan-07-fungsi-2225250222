def jumlah_n(n):
    return sum(range(1, n + 1))

n = int(input("Masukkan bilangan bulat positif: "))

if n > 0:
    print(f"Jumlah bilangan 1 sampai {n}: {jumlah_n(n)}")
else:
    print("Masukkan bilangan positif.")