nilai_global = 100

def contoh_scope():
    nilai_lokal = 50
    print(f"Nilai global: {nilai_global}")
    print(f"Nilai lokal: {nilai_lokal}")

contoh_scope()
print(f"Nilai global di luar fungsi: {nilai_global}")