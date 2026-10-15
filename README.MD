# Audit dan Pembersihan Dataset Daun Cabai

## Deskripsi Proyek

Proyek ini bertujuan untuk melakukan audit dan pembersihan dataset citra daun cabai sebelum digunakan dalam proses pengolahan citra atau pelatihan model *Machine Learning*. Proses audit dilakukan untuk memeriksa file gambar yang rusak, mengidentifikasi duplikat, memastikan kualitas dataset, dan membagi data menjadi data training, validation, dan testing.

Dataset terdiri dari tiga kelas, yaitu **Healthy Leaf**, **Leaf Curl**, dan **Spot Leaf**.

## Struktur Dataset

Dataset awal memiliki 3.000 gambar dengan rincian sebagai berikut:

| Kelas | Jumlah Gambar Awal |
|---|---:|
| Healthy Leaf | 1.000 |
| Leaf Curl | 1.000 |
| Spot Leaf | 1.000 |
| **Total** | **3.000** |

## Tahapan Audit

Proses audit dataset meliputi:

1. **Pemeriksaan file gambar:** memeriksa apakah gambar dapat dibuka dan dibaca.
2. **Pendeteksian duplikat:** menggunakan hash SHA-256 untuk mengidentifikasi file gambar yang memiliki isi identik.
3. **Pembersihan dataset:** mengecualikan file duplikat agar data lebih representatif.
4. **Pemeriksaan duplikat lintas kelas:** mengidentifikasi kelompok gambar identik yang ditemukan pada kelas berbeda untuk ditinjau kembali labelnya.
5. **Pembagian dataset:** membagi data menjadi training, validation, dan testing dengan rasio 70:15:15 menggunakan seed 42.

## Hasil Audit

Berdasarkan hasil audit yang diperoleh, ringkasan dataset adalah sebagai berikut:

| Kelas | Data Unik | Training | Validation | Testing |
|---|---:|---:|---:|---:|
| Healthy Leaf | 564 | 394 | 84 | 86 |
| Leaf Curl | 768 | 537 | 115 | 116 |
| Spot Leaf | 827 | 578 | 124 | 125 |
| **Total** | **2.159** | **1.509** | **323** | **327** |

Hasil pemeriksaan menunjukkan bahwa tidak ditemukan file gambar yang rusak. Selain itu, ditemukan 9 kelompok duplikat lintas kelas yang memerlukan pemeriksaan label secara manual. Sebanyak 817 file duplikat dalam kelas yang sama dikecualikan dalam proses pembersihan.

**Catatan:** Duplikat lintas kelas perlu ditinjau sebelum dataset digunakan untuk pelatihan model agar label kelas tetap konsisten.

## Struktur Repository

```text
audit-dataset-daun-cabai/
├── README.md
├── audit_dataset.py
├── hasil_audit/
│   ├── rekap_dataset_bersih.csv
│   ├── duplikat_lintas_kelas.csv
│   ├── duplikat_dalam_kelas.csv
│   └── file_corrupt.csv
└── laporan/
    └── Laporan_Praktikum_Dataset_Daun_Cabai.pdf
```

Nama file dan struktur folder di atas merupakan struktur yang disarankan. Sesuaikan dengan file yang benar-benar diunggah ke repository.

## Teknologi yang Digunakan

- Python
- Pillow (PIL) untuk membaca dan memeriksa gambar
- SHA-256 untuk identifikasi file identik
- CSV untuk menyimpan laporan hasil audit

## Cara Menjalankan

1. Pastikan Python telah terpasang.
2. Instal pustaka Pillow:

   ```bash
   pip install Pillow
   ```

3. Siapkan dataset dengan struktur folder yang sesuai dengan script audit.
4. Jalankan script Python:

   ```bash
   python audit_dataset.py
   ```

5. Periksa folder hasil audit dan laporan CSV yang dihasilkan.

**Catatan:** Nama script, lokasi input, dan perintah menjalankan perlu disesuaikan jika berbeda dari implementasi sebenarnya.

## Sumber Dataset

Sumber dataset asli: **[Tambahkan tautan dataset yang benar-benar digunakan di sini]**

Dataset awal tidak diubah selama proses audit. Hasil pembersihan dan laporan audit disimpan secara terpisah.

## Informasi

Proyek ini dibuat untuk keperluan praktikum pengolahan citra dan persiapan dataset daun cabai sebelum tahap pelatihan model.
