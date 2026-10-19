# Pertemuan 07 Fungsi Python

**Nama:** Farid Syahputra  
**NIM:** 2225250222  
**Kelas:** 3F

## Tujuan

Menggunakan fungsi, parameter, nilai balik (*return value*), dan *scope* untuk membuat program Python yang modular, terstruktur, dan mudah dipahami.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal pada folder utama repositori:

```bash
python praktik/utilitas_matematika.py
```

## Struktur Fungsi

| Nama Fungsi | Parameter | Nilai Return |
|---|---|---|
| `tambah(a, b)` | Dua bilangan | Hasil penjumlahan |
| `kurang(a, b)` | Dua bilangan | Hasil pengurangan |
| `kali(a, b)` | Dua bilangan | Hasil perkalian |
| `bagi(a, b)` | Dua bilangan | Hasil pembagian; error jika pembagi nol |
| `luas_persegi(sisi)` | Panjang sisi | Luas persegi |
| `luas_persegi_panjang(panjang, lebar)` | Panjang dan lebar | Luas persegi panjang |

## Hasil Pengujian

| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| `tambah(10, 5)` | `15` | `15` | Berhasil |
| `kurang(10, 5)` | `5` | `5` | Berhasil |
| `kali(10, 5)` | `50` | `50` | Berhasil |
| `bagi(10, 5)` | `2.0` | `2.0` | Berhasil |
| `luas_persegi(4)` | `16` | `16` | Berhasil |
| `luas_persegi_panjang(5, 3)` | `15` | `15` | Berhasil |

*Catatan: Hasil aktual di atas sesuai dengan perhitungan kode yang telah dibuat. Jalankan program untuk memverifikasi hasil di komputermu.*

## Refleksi

Pemisahan program menjadi beberapa fungsi membuat kode lebih sederhana dan mudah dipahami. Contohnya, operasi penjumlahan cukup ditulis satu kali dalam fungsi `tambah(a, b)` dan dapat digunakan kembali dengan berbagai nilai. Cara ini mengurangi pengulangan kode, mempermudah pengujian, serta membuat program lebih mudah diperbaiki dan dikembangkan.