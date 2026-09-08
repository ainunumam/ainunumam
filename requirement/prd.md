# DRAF PRD — AgriScan AI

**Sistem Deteksi Dini Penyakit Tanaman Cabai dan Tomat**

## 1. Ringkasan Eksekutif

**AgriScan AI** adalah prototype aplikasi web satu halaman yang membantu petani, penyuluh pertanian, dan pengelola perkebunan hortikultura melakukan **deteksi dini penyakit tanaman cabai dan tomat melalui citra daun/buah**.

Produk berfokus pada enam kategori: **Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, dan Tomat Late Blight**. Sistem menggunakan AI berbasis CNN untuk menghasilkan klasifikasi dan **skor kepercayaan (confidence level)** serta menampilkan visualisasi prapemrosesan citra.

Nilai utama produk bukan sekadar memberikan label penyakit, tetapi membantu pengguna memperoleh **indikasi awal secara lebih cepat dan konsisten** dibandingkan pemeriksaan visual manual. Tantangan utama yang harus diperhatikan adalah penurunan performa ketika digunakan pada kondisi nyata, terutama akibat pencahayaan, kualitas kamera, sudut pengambilan gambar, dan objek di luar kategori yang dikenali.

---

# 2. Problem Statement & Bukti

## Problem Statement

Petani dan praktisi pertanian mengalami risiko kerugian hasil panen karena penyakit tanaman cabai dan tomat dapat **terlambat terdeteksi melalui pemeriksaan manual**. Sistem berbasis citra berpotensi membantu deteksi lebih awal, tetapi performanya di lapangan dapat menurun dibandingkan hasil pengujian pada dataset.

### Fakta

| Fakta                                                                  | Bukti dari konteks                                                                                   |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Terdapat enam kelas penyakit/kondisi tanaman yang menjadi target       | Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight |
| Dataset berjumlah 3.734 citra                                          | Gabungan PlantVillage dan dataset mandiri                                                            |
| Akurasi model pada data latih/validasi mencapai 91%                    | Terjadi pada epoch 18–20                                                                             |
| Akurasi dataset uji mencapai 91%                                       | Berdasarkan riset yang diberikan                                                                     |
| Akurasi turun menjadi 75% pada pengujian nyata                         | Pengujian melalui aplikasi web menggunakan 60 sampel                                                 |
| Penyebab penurunan performa                                            | Pencahayaan, sudut/kualitas gambar, dan tidak adanya mekanisme OOD                                   |
| Cabai Leaf Curl memiliki kesalahan deteksi tinggi pada pengujian nyata | Kesalahan mencapai 50%                                                                               |
| Tomat Normal mengalami kesalahan deteksi                               | Kesalahan mencapai 40%                                                                               |
| Early Blight dan Late Blight memiliki kemiripan visual                 | Terdapat 14 sampel salah pada dataset uji                                                            |
| Recall Tomat Late Blight merupakan yang terendah                       | Recall 0,7594; F1-Score 0,8510                                                                       |
| Cabai Leaf Curl memiliki performa metrik tinggi                        | Precision 0,9711; Recall 0,9619                                                                      |

### Asumsi

* **[ASUMSI-01]** Pengguna memiliki smartphone Android dengan kamera yang cukup untuk mengambil foto tanaman.
* **[ASUMSI-02]** Pengguna dapat mengakses aplikasi web meskipun koneksi internet di lapangan terbatas.
* **[ASUMSI-03]** Pengguna memahami bahwa hasil AI merupakan **indikasi awal**, bukan diagnosis definitif.
* **[ASUMSI-04]** Data yang tersedia untuk prototype belum cukup untuk mewakili seluruh variasi kondisi lapangan.
* **[ASUMSI-05]** Pengujian prototype selama tiga bulan dapat dilakukan menggunakan data dan sumber daya yang tersedia.

---

# 3. Target User & Stakeholder

| Peran                                      | Kebutuhan                                                       | Pengaruh                    |
| ------------------------------------------ | --------------------------------------------------------------- | --------------------------- |
| **Petani cabai & tomat**                   | Mengetahui indikasi awal kondisi tanaman dengan cepat dan mudah | **Tinggi** — pengguna utama |
| **Penyuluh pertanian lapangan**            | Membantu pemeriksaan dan memberikan indikasi awal kepada petani | **Tinggi**                  |
| **Pengelola perkebunan hortikultura**      | Memantau kondisi tanaman secara lebih terstruktur               | **Tinggi**                  |
| **Tim Developer Web/AI**                   | Mengembangkan dan menyempurnakan prototype                      | **Tinggi**                  |
| **Peneliti/Pakar Hama & Penyakit Tanaman** | Memvalidasi kesesuaian kategori dan hasil deteksi               | **Tinggi**                  |
| **Pengelola Platform/Mitra Pertanian**     | Mendukung penggunaan dan keberlanjutan platform                 | **Sedang–Tinggi**           |

---

# 4. Value Proposition

### Pain yang Dikurangi

1. Deteksi penyakit secara manual membutuhkan pengamatan langsung dan berpotensi terlambat.
2. Pengguna dapat kesulitan membedakan penyakit yang memiliki kemiripan visual.
3. Kualitas hasil pemeriksaan citra dapat berbeda karena pencahayaan, sudut, dan kualitas kamera.
4. Model yang baik pada dataset belum tentu memiliki performa yang sama di lapangan.
5. Pengguna membutuhkan cara yang lebih praktis untuk memperoleh **indikasi awal** kondisi tanaman.

### Gain yang Diciptakan

1. **Deteksi awal lebih cepat** melalui foto tanaman.
2. Memberikan klasifikasi kondisi/penyakit dari enam kategori target.
3. Memberikan **confidence level** agar pengguna mengetahui tingkat keyakinan hasil prediksi.
4. Menampilkan visualisasi prapemrosesan untuk membantu memahami citra yang dianalisis.
5. Membantu penyuluh atau pengelola perkebunan melakukan pemeriksaan awal secara lebih konsisten.

### Mengapa AI Bukan Gimmick?

AI menjadi bagian inti karena fungsi utama produk adalah **menginterpretasikan citra tanaman dan mengklasifikasikan kondisi visualnya**. Tanpa model AI, aplikasi hanya menjadi media untuk mengambil atau menampilkan gambar.

Namun, AI tidak diposisikan sebagai pengganti pakar. Hasilnya digunakan sebagai **alat bantu deteksi dini**, terutama karena riset menunjukkan performa pada kondisi nyata masih lebih rendah daripada performa pada dataset.

---

# 5. Tujuan Produk & KPI Terukur

## Tujuan Produk

1. Menyediakan alat bantu deteksi dini penyakit cabai dan tomat berbasis citra.
2. Menghasilkan klasifikasi untuk enam kategori target.
3. Menampilkan confidence level pada setiap hasil prediksi.
4. Mengidentifikasi dan mengevaluasi kesenjangan performa antara pengujian dataset dan kondisi nyata.
5. Menghasilkan prototype yang dapat diselesaikan dalam periode tiga bulan.

## KPI

| KPI                                      |                    Target 3 Bulan | Cara Mengukur                                                 |
| ---------------------------------------- | --------------------------------: | ------------------------------------------------------------- |
| **Akurasi klasifikasi pada dataset uji** |      ≥ 91% sebagai benchmark awal | Jumlah prediksi benar ÷ seluruh sampel uji × 100%             |
| **Akurasi pada pengujian nyata**         |       ≥ 75% sebagai baseline awal | Jumlah prediksi benar ÷ seluruh sampel pengujian nyata × 100% |
| **Confidence level**                     | Tersedia pada 100% hasil prediksi | Persentase hasil prediksi yang menampilkan skor kepercayaan   |
| **Cakupan kelas**                        |                         6/6 kelas | Jumlah kategori target yang dapat diprediksi                  |
| **Pengujian kondisi nyata**              |                       ≥ 60 sampel | Jumlah citra yang diuji melalui penggunaan kamera             |
| **Evaluasi per kelas**                   |              6/6 kelas dievaluasi | Precision, recall, dan F1-Score setiap kelas                  |
| **Penyelesaian prototype**               |                         ≤ 3 bulan | Perbandingan tanggal mulai dan prototype siap diuji           |

> **Catatan:** Target ≥75% untuk pengujian nyata menggunakan hasil 75% pada riset sebagai **baseline**, bukan klaim bahwa prototype baru pasti mencapai angka tersebut.

---

# 6. Scope Fitur 3 Bulan — MoSCoW

| Prioritas       | Fitur                                        | Deskripsi                                                                                            |
| --------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Must Have**   | ★ **Deteksi penyakit berbasis citra**        | Mengklasifikasikan citra tanaman cabai/tomat ke dalam enam kategori target                           |
| **Must Have**   | ★ **Confidence level**                       | Menampilkan tingkat kepercayaan terhadap hasil klasifikasi                                           |
| **Must Have**   | ★ **Klasifikasi 6 kelas**                    | Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight |
| **Must Have**   | ★ **Visualisasi prapemrosesan**              | Menampilkan hasil prapemrosesan citra sebagai bagian dari proses deteksi                             |
| **Must Have**   | **Pengambilan/upload citra**                 | Pengguna dapat memberikan citra tanaman untuk dianalisis                                             |
| **Must Have**   | **Tampilan hasil deteksi**                   | Menampilkan kategori hasil dan confidence level secara jelas                                         |
| **Should Have** | ★ **Peringatan hasil berkepercayaan rendah** | Membantu pengguna memahami bahwa hasil dengan confidence rendah perlu diperiksa kembali              |
| **Should Have** | ★ **Penanganan indikasi OOD**                | Membantu mengurangi risiko sistem memaksakan klasifikasi pada objek yang tidak sesuai kategori       |
| **Should Have** | **Panduan pengambilan gambar**               | Membantu pengguna memperoleh citra yang lebih sesuai untuk pemeriksaan                               |
| **Could Have**  | **Riwayat hasil deteksi**                    | Menyimpan hasil pemeriksaan sebelumnya untuk kebutuhan pemantauan                                    |
| **Could Have**  | **Informasi ringkas penyakit**               | Menampilkan informasi dasar mengenai kategori yang terdeteksi                                        |
| **Could Have**  | **Dashboard sederhana**                      | Ringkasan hasil pemeriksaan yang telah dilakukan                                                     |
| **Won't Have**  | Diagnosis definitif                          | Sistem tidak menetapkan diagnosis final sebagai pengganti pakar                                      |
| **Won't Have**  | Rekomendasi pengobatan otomatis              | Tidak menjadi fokus prototype tiga bulan                                                             |
| **Won't Have**  | Prediksi hasil panen                         | Tidak termasuk ruang lingkup produk                                                                  |
| **Won't Have**  | Pemantauan seluruh jenis tanaman             | Fokus hanya cabai dan tomat                                                                          |

**Keterangan:** ★ = fitur yang menggunakan atau berkaitan langsung dengan AI.

---

# 7. Non-Goals Eksplisit

AgriScan AI **tidak bertujuan untuk**:

1. Menggantikan peran pakar penyakit tanaman atau penyuluh pertanian.
2. Memberikan diagnosis penyakit secara definitif.
3. Memberikan rekomendasi pestisida atau dosis pengobatan secara otomatis.
4. Mendeteksi seluruh penyakit tanaman cabai dan tomat.
5. Mendukung seluruh jenis tanaman pada prototype awal.
6. Menjamin akurasi yang sama antara dataset dan kondisi lapangan.
7. Menjadi sistem pemantauan perkebunan berskala besar secara penuh.
8. Mengembangkan infrastruktur AI yang kompleks di luar kebutuhan prototype tiga bulan.
9. Menyelesaikan seluruh permasalahan OOD dalam kondisi lapangan.

---

# 8. Asumsi & Risiko Utama + Mitigasi

| Risiko/Asumsi                                                           | Dampak                                                 | Mitigasi                                                                                            |
| ----------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| **[ASUMSI-01]** Kamera smartphone pengguna memiliki kualitas yang cukup | Citra buruk dapat menyebabkan salah klasifikasi        | Memberikan panduan pengambilan gambar dan mengevaluasi citra nyata                                  |
| Variasi pencahayaan tinggi                                              | Akurasi dapat turun di lapangan                        | Menguji citra pada kondisi nyata yang beragam dan mengevaluasi hasil per kelas                      |
| Sudut pengambilan gambar berbeda                                        | Karakteristik objek dapat berubah                      | Memberikan panduan posisi pengambilan gambar                                                        |
| Kualitas kamera berbeda-beda                                            | Model dapat menghasilkan prediksi yang tidak konsisten | Pengujian menggunakan beberapa kondisi kualitas citra                                               |
| **OOD belum tertangani dengan baik**                                    | Sistem dapat memaksakan salah satu dari enam kelas     | Memprioritaskan mekanisme indikasi/penanganan OOD pada fitur Should Have                            |
| Kemiripan Early Blight dan Late Blight                                  | Salah klasifikasi dapat terjadi                        | Evaluasi khusus terhadap kedua kelas dan pemantauan precision/recall/F1                             |
| Recall Tomat Late Blight rendah                                         | Penyakit dapat lebih sering terlewatkan                | Menjadikan recall kelas ini sebagai metrik pemantauan utama                                         |
| Cabai Leaf Curl memiliki error tinggi pada kondisi nyata                | Hasil deteksi lapangan kurang dapat diandalkan         | Pengujian dan evaluasi khusus pada kelas Cabai Leaf Curl                                            |
| Data pelatihan terbatas                                                 | Kemampuan generalisasi model terbatas                  | Fokus pada enam kelas dan evaluasi menggunakan data nyata yang tersedia                             |
| **[ASUMSI-02]** Koneksi internet terbatas                               | Penggunaan aplikasi dapat terganggu                    | Menjaga proses penggunaan tetap ringan sesuai batasan prototype                                     |
| Waktu pengembangan hanya 3 bulan                                        | Fitur terlalu banyak dapat mengganggu fokus            | Menggunakan prioritas MoSCoW dan menempatkan fitur tambahan sebagai Could Have                      |
| Anggaran infrastruktur AI terbatas                                      | Pengembangan skala besar tidak memungkinkan            | Membatasi scope pada kebutuhan inti prototype                                                       |
| **[ASUMSI-03]** Pengguna memahami hasil AI sebagai indikasi awal        | Risiko keputusan yang salah jika hasil dianggap mutlak | Menampilkan confidence level dan penjelasan bahwa hasil perlu dipertimbangkan sebagai indikasi awal |

---

## Ringkasan Prioritas Produk

**Fokus utama AgriScan AI selama tiga bulan adalah:**

> **Foto tanaman → analisis AI → klasifikasi 6 kelas → confidence level → visualisasi hasil → pengguna memperoleh indikasi awal.**

Prioritas keberhasilan bukan hanya mengejar angka akurasi tinggi pada dataset, tetapi **mengukur dan mengurangi gap antara performa model pada dataset (91%) dan penggunaan nyata (75%)**, khususnya pada **Cabai Leaf Curl, Tomat Normal, serta Tomat Early Blight/Late Blight**, karena area tersebut menunjukkan masalah paling nyata berdasarkan bukti riset yang tersedia.
