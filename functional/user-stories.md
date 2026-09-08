# DRAF User Stories — AgriScan AI

Berikut penurunan **User Stories** dari SRS AgriScan AI. User Stories hanya mencakup fitur **Must Have** dan **Should Have**, serta setiap story memiliki keterlacakan langsung ke FR dan, bila relevan, NFR/BR.

---

# Epik 1 — Penginputan & Panduan Citra

### US-01 — Pengambilan/Pengunggahan Citra

* **ID User Story**: US-01
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **mengambil atau mengunggah citra tanaman cabai atau tomat**, Sehingga **saya dapat memberikan citra tanaman untuk dianalisis oleh AgriScan AI**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-01**, NFR-08, AS-01.

### US-02 — Input Citra oleh Penyuluh

* **ID User Story**: US-02
* **Pernyataan**: "Sebagai **Penyuluh Pertanian**, Saya ingin **mengambil atau mengunggah citra tanaman cabai atau tomat**, Sehingga **saya dapat menggunakan citra tersebut sebagai dasar pemeriksaan awal tanaman**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-01**, NFR-08, AS-02.

### US-03 — Panduan Pengambilan Citra

* **ID User Story**: US-03
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **melihat panduan pengambilan citra sebelum melakukan deteksi**, Sehingga **saya dapat menghasilkan citra yang lebih sesuai untuk dianalisis oleh sistem**."
* **Prioritas**: **Should Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-09**, NFR-10, NFR-12, BR-05.

### US-04 — Panduan Citra untuk Pemeriksaan Lapangan

* **ID User Story**: US-04
* **Pernyataan**: "Sebagai **Penyuluh Pertanian**, Saya ingin **melihat panduan pengambilan citra**, Sehingga **saya dapat mengambil citra dengan kondisi yang lebih sesuai ketika melakukan pemeriksaan lapangan**."
* **Prioritas**: **Should Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-09**, NFR-10, NFR-12.

---

# Epik 2 — Analisis & Klasifikasi AI

### US-05 — Analisis Citra Tanaman

* **ID User Story**: US-05
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **menganalisis citra tanaman menggunakan AI**, Sehingga **saya dapat memperoleh indikasi awal kondisi tanaman dengan lebih cepat**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-02**, NFR-01, NFR-02, NFR-07.

### US-06 — Klasifikasi Enam Kategori

* **ID User Story**: US-06
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **mendapatkan klasifikasi kondisi tanaman berdasarkan enam kategori target**, Sehingga **saya dapat mengetahui indikasi kondisi tanaman cabai atau tomat yang diperiksa**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-03**, NFR-03, BR-04.

### US-07 — Analisis untuk Penyuluh

* **ID User Story**: US-07
* **Pernyataan**: "Sebagai **Penyuluh Pertanian**, Saya ingin **menganalisis citra tanaman menggunakan AI**, Sehingga **saya dapat memperoleh alat bantu dalam melakukan pemeriksaan awal tanaman di lapangan**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-02**, NFR-07, NFR-12.

### US-08 — Analisis untuk Pengelola Perkebunan

* **ID User Story**: US-08
* **Pernyataan**: "Sebagai **Pengelola Perkebunan**, Saya ingin **menganalisis citra tanaman cabai dan tomat**, Sehingga **saya dapat memperoleh indikasi awal kondisi tanaman untuk mendukung pemantauan**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-02**, FR-03, NFR-03.

### US-09 — Confidence Level

* **ID User Story**: US-09
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **mendapatkan confidence level dari setiap hasil klasifikasi**, Sehingga **saya dapat mengetahui tingkat keyakinan sistem terhadap hasil prediksi**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-04**, NFR-09, BR-01.

### US-10 — Peringatan Confidence Rendah

* **ID User Story**: US-10
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **mendapatkan peringatan ketika hasil klasifikasi memiliki confidence rendah**, Sehingga **saya tidak langsung menganggap hasil tersebut sebagai indikasi yang meyakinkan**."
* **Prioritas**: **Should Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-07**, BR-01, BR-03.

### US-11 — Indikasi OOD

* **ID User Story**: US-11
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **mendapatkan indikasi ketika citra berpotensi berada di luar kategori yang dikenali sistem**, Sehingga **saya mengetahui bahwa hasil klasifikasi tersebut tidak dapat dipercaya sebagai klasifikasi target**."
* **Prioritas**: **Should Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-08**, BR-02, BR-04.

### US-12 — Indikasi OOD untuk Penyuluh

* **ID User Story**: US-12
* **Pernyataan**: "Sebagai **Penyuluh Pertanian**, Saya ingin **mengetahui ketika citra berpotensi merupakan objek di luar kategori yang dikenali**, Sehingga **saya dapat mempertimbangkan hasil AI secara lebih hati-hati dalam pemeriksaan lapangan**."
* **Prioritas**: **Should Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-08**, BR-02, BR-03.

---

# Epik 3 — Penyajian Hasil & Transparansi AI

### US-13 — Melihat Hasil Deteksi

* **ID User Story**: US-13
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **melihat hasil klasifikasi dan confidence level setelah citra dianalisis**, Sehingga **saya dapat memperoleh indikasi awal kondisi tanaman yang diperiksa**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-05**, FR-04, NFR-09.

### US-14 — Visualisasi Prapemrosesan

* **ID User Story**: US-14
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **melihat visualisasi prapemrosesan citra**, Sehingga **saya dapat melihat representasi citra yang digunakan dalam proses analisis**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-06**.

### US-15 — Transparansi Hasil AI

* **ID User Story**: US-15
* **Pernyataan**: "Sebagai **Petani**, Saya ingin **melihat informasi bahwa hasil AI merupakan indikasi awal**, Sehingga **saya tidak menganggap hasil klasifikasi sebagai diagnosis penyakit yang definitif**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-10**, NFR-11, NFR-15, BR-03.

### US-16 — Transparansi untuk Penyuluh

* **ID User Story**: US-16
* **Pernyataan**: "Sebagai **Penyuluh Pertanian**, Saya ingin **melihat batasan penggunaan hasil AI**, Sehingga **saya dapat menggunakan hasil sistem sebagai alat bantu pemeriksaan dan bukan sebagai pengganti penilaian pakar**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-10**, NFR-11, NFR-15, BR-03.

---

# Epik 4 — Evaluasi & Performa Sistem

### US-17 — Evaluasi Enam Kelas

* **ID User Story**: US-17
* **Pernyataan**: "Sebagai **Tim Developer**, Saya ingin **mengevaluasi performa model pada keenam kelas menggunakan Precision, Recall, dan F1-Score**, Sehingga **saya dapat mengetahui performa model pada setiap kategori target**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-11**, NFR-03, NFR-04, BR-05.

### US-18 — Evaluasi Dataset Uji

* **ID User Story**: US-18
* **Pernyataan**: "Sebagai **Tim Developer**, Saya ingin **mengukur akurasi model pada dataset uji**, Sehingga **saya dapat memastikan performa model mencapai target minimal 91%**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-11**, NFR-01.

### US-19 — Evaluasi Real-World

* **ID User Story**: US-19
* **Pernyataan**: "Sebagai **Tim Developer**, Saya ingin **menguji model menggunakan citra nyata melalui aplikasi web**, Sehingga **saya dapat mengetahui performa model pada kondisi penggunaan lapangan**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-12**, NFR-02, NFR-12.

### US-20 — Pemantauan Tomat Late Blight

* **ID User Story**: US-20
* **Pernyataan**: "Sebagai **Tim Developer**, Saya ingin **memantau Recall dan F1-Score kelas Tomat Late Blight**, Sehingga **saya dapat mengetahui apakah performa kelas yang memiliki recall terendah mengalami perbaikan atau penurunan**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-11**, NFR-05, BR-05.

### US-21 — Evaluasi Cabai Leaf Curl

* **ID User Story**: US-21
* **Pernyataan**: "Sebagai **Tim Developer**, Saya ingin **mengevaluasi performa klasifikasi Cabai Leaf Curl secara khusus**, Sehingga **saya dapat mengetahui dan memantau masalah kesalahan deteksi yang tinggi pada pengujian nyata**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-11**, NFR-06, BR-05.

### US-22 — Evaluasi Early Blight dan Late Blight

* **ID User Story**: US-22
* **Pernyataan**: "Sebagai **Tim Developer**, Saya ingin **mengevaluasi kesalahan klasifikasi antara Tomat Early Blight dan Tomat Late Blight**, Sehingga **saya dapat memantau masalah klasifikasi pada dua kategori yang memiliki kemiripan visual**."
* **Prioritas**: **Must Have**
* **Keterlacakan (Traceability)**: Diturunkan dari: **FR-11**, NFR-04, NFR-05, BR-05.

---

# Rekapitulasi User Stories

| Epik       | ID    | Fokus                         | Prioritas   |
| ---------- | ----- | ----------------------------- | ----------- |
| **Epik 1** | US-01 | Input citra                   | Must Have   |
|            | US-02 | Input citra penyuluh          | Must Have   |
|            | US-03 | Panduan citra petani          | Should Have |
|            | US-04 | Panduan citra penyuluh        | Should Have |
| **Epik 2** | US-05 | Analisis AI                   | Must Have   |
|            | US-06 | Klasifikasi 6 kelas           | Must Have   |
|            | US-07 | Analisis AI penyuluh          | Must Have   |
|            | US-08 | Analisis AI perkebunan        | Must Have   |
|            | US-09 | Confidence level              | Must Have   |
|            | US-10 | Peringatan confidence rendah  | Should Have |
|            | US-11 | Indikasi OOD                  | Should Have |
|            | US-12 | OOD untuk penyuluh            | Should Have |
| **Epik 3** | US-13 | Hasil deteksi                 | Must Have   |
|            | US-14 | Visualisasi preprocessing     | Must Have   |
|            | US-15 | Batas klaim AI                | Must Have   |
|            | US-16 | Transparansi untuk penyuluh   | Must Have   |
| **Epik 4** | US-17 | Evaluasi 6 kelas              | Must Have   |
|            | US-18 | Evaluasi dataset              | Must Have   |
|            | US-19 | Real-world testing            | Must Have   |
|            | US-20 | Evaluasi Late Blight          | Must Have   |
|            | US-21 | Evaluasi Leaf Curl            | Must Have   |
|            | US-22 | Evaluasi Early vs Late Blight | Must Have   |

### Ringkasan Prioritas

* **Must Have:** 17 User Stories
* **Should Have:** 5 User Stories
* **Could Have:** 0
* **Won't Have:** 0

Dengan demikian, seluruh User Story tetap berada dalam batas SRS: **input citra → analisis CNN → klasifikasi enam kelas → confidence → penyajian hasil → transparansi → evaluasi performa**, tanpa masuk ke detail arsitektur teknis atau desain UI.
