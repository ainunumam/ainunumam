# DRAFT Use Case & Acceptance Criteria — AgriScan AI

Dokumen berikut menurunkan **UC-01** dan Acceptance Criteria untuk **seluruh US-01 s.d. US-22**. Angka yang digunakan mengikuti SRS/aturan bisnis yang diberikan: **6 kelas target, ukuran file ≤5 MB, latensi ≤3,0 detik, confidence 70%, OOD <50%, akurasi dataset ≥91%, dan real-world ≥75% dari minimal 60 sampel**.

---

# BAGIAN 1 — USE CASE DETAIL

## UC-01 — Deteksi Dini Penyakit Tanaman Cabai dan Tomat

| Elemen                | Spesifikasi                                                                                                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ID Use Case**       | **UC-01**                                                                                                                                                                                |
| **Nama Use Case**     | **Deteksi Dini Penyakit Tanaman Cabai dan Tomat**                                                                                                                                        |
| **Aktor Utama**       | Petani / Penyuluh Pertanian                                                                                                                                                              |
| **Tujuan**            | Memperoleh indikasi awal kondisi tanaman cabai/tomat berdasarkan citra                                                                                                                   |
| **Pre-kondisi**       | Pengguna mengakses aplikasi web AgriScan AI melalui browser smartphone/PC; berkas citra tanaman berformat JPG/JPEG/PNG dengan ukuran **≤5 MB** siap diunggah atau diambil melalui kamera |
| **Post-kondisi**      | Sistem menampilkan hasil klasifikasi dari **6 kelas target**, confidence level (%), visualisasi prapemrosesan, dan penafian wajib                                                        |
| **Prioritas**         | Must Have                                                                                                                                                                                |
| **User Stories**      | US-01, US-05, US-06, US-09, US-13, US-14, US-15                                                                                                                                          |
| **Batas klasifikasi** | Tepat 6 kelas: Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight                                                                      |
| **Target latensi**    | ≤ **3,0 detik** untuk inferensi AI                                                                                                                                                       |
| **Confidence tinggi** | ≥ **70%**                                                                                                                                                                                |
| **Confidence rendah** | < **70%**                                                                                                                                                                                |
| **Indikasi OOD**      | Confidence < **50%** atau objek berada di luar 6 kelas target                                                                                                                            |

---

## 1.1 Skenario Utama — Happy Flow

|    No. | Aktor                                                      | Respons Sistem                                                                                               |
| -----: | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
|  **1** | Petani/Penyuluh membuka AgriScan AI.                       | Sistem menampilkan fungsi untuk mengambil atau mengunggah citra.                                             |
|  **2** | Pengguna mengambil foto atau memilih berkas citra tanaman. | Sistem menerima citra untuk validasi.                                                                        |
|  **3** | —                                                          | Sistem memeriksa ekstensi dan ukuran berkas.                                                                 |
|  **4** | —                                                          | Jika format JPG/JPEG/PNG dan ukuran **≤5 MB**, sistem menerima citra.                                        |
|  **5** | Pengguna menjalankan deteksi.                              | Sistem menampilkan status pemrosesan.                                                                        |
|  **6** | —                                                          | Sistem melakukan prapemrosesan citra.                                                                        |
|  **7** | —                                                          | Sistem menjalankan analisis AI menggunakan model CNN.                                                        |
|  **8** | —                                                          | Sistem menghasilkan kelas prediksi dan confidence level.                                                     |
|  **9** | —                                                          | Sistem memeriksa confidence dan status OOD.                                                                  |
| **10** | —                                                          | Jika confidence **≥70%** dan tidak terindikasi OOD, sistem menetapkan hasil sebagai indikasi dominan.        |
| **11** | —                                                          | Sistem menampilkan satu dari **6 kelas target** dan confidence dalam persen.                                 |
| **12** | —                                                          | Sistem menampilkan visualisasi prapemrosesan citra.                                                          |
| **13** | —                                                          | Sistem menampilkan disclaimer: **"Hasil AI merupakan indikasi awal, bukan diagnosis definitif dari pakar."** |
| **14** | Pengguna                                                   | Pengguna membaca hasil sebagai indikasi awal kondisi tanaman.                                                |
| **15** | —                                                          | Use case selesai. Seluruh proses inferensi ditargetkan selesai dalam **≤3,0 detik**.                         |

---

# 1.2 Skenario Alternatif / Eksepsi

## A1 — Format atau Ukuran Berkas Tidak Valid

**Kondisi:**

* Format bukan JPG/JPEG/PNG; atau
* Ukuran file **>5 MB**.

**Respons:**

1. Sistem menolak citra.
2. Sistem tidak menjalankan inferensi AI.
3. Sistem memberikan informasi mengenai ketentuan file.
4. Pengguna diminta memilih/mengambil citra lain.

---

## A2 — Confidence Rendah

**Kondisi:**

> **50% ≤ confidence <70%**

**Respons:**

1. Sistem menampilkan hasil klasifikasi.
2. Sistem menampilkan confidence level.
3. Sistem memberikan peringatan:

> **"Hasil Meragukan / Confidence Rendah."**

4. Sistem tetap menampilkan disclaimer wajib.
5. Hasil tidak boleh dianggap sebagai diagnosis definitif.

---

## A3 — Indikasi OOD

**Kondisi:**

> **Confidence <50%** atau citra terindikasi berada di luar enam kelas target.

**Respons:**

1. Sistem memberikan indikasi **OOD**.
2. Sistem memberi tahu pengguna bahwa objek tidak dikenali/tidak dapat dipercaya sebagai salah satu dari enam kelas target.
3. Sistem tidak memberikan diagnosis definitif.
4. Disclaimer tetap ditampilkan.

> **Prioritas aturan:** Jika confidence = 45%, kondisi `<70%` dan `<50%` sama-sama terpenuhi. Sistem harus memprioritaskan status **OOD** sesuai BR-02.

---

## A4 — Timeout / Kegagalan Server

**Kondisi:**

> Waktu inferensi **>3,0 detik**, server Flask gagal, koneksi terputus, atau proses AI mengalami kegagalan.

**Respons:**

1. Sistem tidak menampilkan prediksi sebagai hasil yang berhasil.
2. Sistem menampilkan pesan kegagalan yang dapat dipahami pengguna.
3. Sistem menyediakan opsi **Coba Lagi**.
4. Pengguna dapat mengulangi proses.

---

# BAGIAN 2 — ACCEPTANCE CRITERIA GHERKIN

## EPIC 1 — Penginputan & Panduan Citra

---

## US-01 — Pengambilan/Pengunggahan Citra oleh Petani

**User Story:** Sebagai Petani, Saya ingin mengambil atau mengunggah citra tanaman cabai atau tomat sehingga citra dapat dianalisis.

### AC-01.1 — Happy Path

**Given**

* Petani membuka AgriScan AI.
* Petani memiliki citra tanaman berformat **JPG**.
* Ukuran file adalah **≤5 MB**.

**When**

* Petani mengambil atau mengunggah citra.

**Then**

* Sistem menerima citra.
* Citra tersedia untuk proses analisis AI.

**Metode uji:** Integration Test + UAT.

### AC-01.2 — Boundary File 5 MB

**Given**

* Petani memilih citra JPG berukuran tepat **5 MB**.

**When**

* Citra diunggah.

**Then**

* Sistem menerima citra karena ukuran **≤5 MB**.

**Metode uji:** Boundary Value Analysis.

### AC-01.3 — File >5 MB

**Given**

* Petani memilih citra PNG berukuran **5,01 MB**.

**When**

* Citra diunggah.

**Then**

* Sistem menolak citra.
* Sistem tidak memulai analisis AI.

**Metode uji:** Boundary Value Analysis.

---

## US-02 — Pengambilan/Pengunggahan Citra oleh Penyuluh

### AC-02.1 — Happy Path

**Given**

* Penyuluh membuka aplikasi.
* Penyuluh memilih citra tanaman berformat PNG berukuran **≤5 MB**.

**When**

* Penyuluh mengunggah citra.

**Then**

* Sistem menerima citra untuk pemeriksaan awal.

**Metode uji:** Integration Test + UAT.

### AC-02.2 — Boundary 5 MB

**Given**

* Citra berformat JPG/JPEG/PNG dengan ukuran tepat **5 MB**.

**When**

* Penyuluh mengunggah citra.

**Then**

* Sistem menerima citra.

**Metode uji:** Boundary Value Analysis.

### AC-02.3 — Format Tidak Valid

**Given**

* Penyuluh memilih file PDF berukuran **2 MB**.

**When**

* Penyuluh mengunggah file.

**Then**

* Sistem menolak file karena bukan JPG/JPEG/PNG.

**Metode uji:** Negative Test.

---

## US-03 — Panduan Pengambilan Citra oleh Petani

### AC-03.1 — Panduan Tersedia

**Given**

* Petani membuka fungsi input citra.

**When**

* Petani mengakses panduan pengambilan gambar.

**Then**

* Sistem menampilkan panduan pengambilan citra sebelum deteksi.

**Metode uji:** UAT + Inspection.

### AC-03.2 — Panduan Sebelum Deteksi

**Given**

* Petani belum memulai proses analisis.

**When**

* Petani membuka bagian pengambilan citra.

**Then**

* Panduan dapat diakses sebelum citra dikirim untuk analisis.

**Metode uji:** UAT.

---

## US-04 — Panduan Pengambilan Citra oleh Penyuluh

### AC-04.1 — Panduan Dapat Diakses

**Given**

* Penyuluh membuka fungsi input citra.

**When**

* Penyuluh memilih panduan pengambilan citra.

**Then**

* Sistem menampilkan panduan.

**Metode uji:** UAT.

### AC-04.2 — Panduan Sebelum Pengiriman

**Given**

* Penyuluh belum mengirim citra untuk analisis.

**When**

* Penyuluh mengakses panduan.

**Then**

* Panduan tersedia sebelum proses analisis dimulai.

**Metode uji:** Inspection + UAT.

---

# EPIC 2 — Analisis & Klasifikasi AI

> Untuk seluruh User Story AI di bawah, pengujian latensi menggunakan batas **≤3,0 detik**. Pengujian boundary dilakukan pada nilai **3,0 detik** dan kondisi timeout **>3,0 detik**.

---

## US-05 — Analisis Citra Menggunakan AI

### AC-05.1 — Happy Path

**Given**

* Citra valid berformat JPG/PNG berukuran **≤5 MB**.
* Citra termasuk salah satu dari 6 kelas target.

**When**

* Petani menjalankan deteksi.

**Then**

* Sistem melakukan inferensi CNN.
* Hasil tersedia dalam waktu **≤3,0 detik**.
* Sistem menghasilkan klasifikasi dan confidence level.

**Metode uji:** Integration Test + Performance Test.

### AC-05.2 — Boundary Latensi

**Given**

* Citra valid tersedia.
* Waktu inferensi tepat **3,0 detik**.

**When**

* Sistem menyelesaikan inferensi.

**Then**

* Proses dinyatakan memenuhi batas NFR-07 karena waktu **≤3,0 detik**.
* Hasil klasifikasi ditampilkan.

**Metode uji:** Performance/Boundary Test.

### AC-05.3 — Timeout

**Given**

* Citra valid tersedia.
* Inferensi membutuhkan **3,01 detik** atau lebih.

**When**

* Batas waktu 3,0 detik terlampaui.

**Then**

* Sistem tidak menganggap proses sebagai respons yang memenuhi target latensi.
* Sistem menampilkan status kegagalan/timeout dan menyediakan mekanisme mencoba kembali.

**Metode uji:** Performance Test + Negative Test.

---

## US-06 — Klasifikasi Enam Kelas

### AC-06.1 — Happy Path

**Given**

* Citra valid telah dianalisis.
* Model menghasilkan confidence **≥70%**.

**When**

* Sistem menyelesaikan klasifikasi.

**Then**

* Sistem menghasilkan tepat **1 kelas** dari **6 kelas target**.

**Metode uji:** Integration Test + UAT.

### AC-06.2 — Boundary Confidence 70%

**Given**

* Sistem menghasilkan confidence tepat **70%**.

**When**

* Sistem menentukan status hasil.

**Then**

* Hasil dikategorikan sebagai **High Confidence/indikasi dominan**.
* Hasil tetap berada dalam 6 kelas target.

**Metode uji:** Boundary Value Analysis.

### AC-06.3 — Confidence 69,99%

**Given**

* Sistem menghasilkan confidence **69,99%**.

**When**

* Sistem menentukan status hasil.

**Then**

* Sistem memberikan status **Hasil Meragukan / Confidence Rendah**.

**Metode uji:** Boundary Value Analysis.

### AC-06.4 — Timeout

**Given**

* Citra valid tersedia.
* Inferensi membutuhkan **>3,0 detik**.

**When**

* Batas waktu terlampaui.

**Then**

* Sistem tidak menyatakan proses sebagai deteksi berhasil.

**Metode uji:** Performance Test.

---

## US-07 — Analisis AI untuk Penyuluh

### AC-07.1 — Happy Path

**Given**

* Penyuluh memberikan citra JPG/PNG dengan ukuran **≤5 MB**.
* Citra dapat dianalisis.

**When**

* Penyuluh menjalankan deteksi.

**Then**

* Sistem menghasilkan klasifikasi dan confidence dalam waktu **≤3,0 detik**.

**Metode uji:** Integration Test + UAT.

### AC-07.2 — Boundary Latensi

**Given**

* Inferensi selesai tepat dalam **3,0 detik**.

**When**

* Sistem menampilkan hasil.

**Then**

* Respons memenuhi batas NFR-07.

**Metode uji:** Performance Test.

### AC-07.3 — Timeout

**Given**

* Inferensi berlangsung selama **3,01 detik**.

**When**

* Batas 3,0 detik terlampaui.

**Then**

* Sistem menampilkan status timeout/error dan tidak menyatakan deteksi berhasil.

**Metode uji:** Performance Test.

---

## US-08 — Analisis AI untuk Pengelola Perkebunan

### AC-08.1 — Happy Path

**Given**

* Pengelola memberikan citra valid ≤**5 MB**.
* Format JPG/PNG.
* Citra termasuk salah satu dari 6 kelas target.

**When**

* Pengelola menjalankan analisis.

**Then**

* Sistem menghasilkan salah satu dari **6 kelas** dan confidence dalam waktu **≤3,0 detik**.

**Metode uji:** Integration Test + UAT.

### AC-08.2 — Boundary 5 MB

**Given**

* Citra berukuran tepat **5 MB** dan berformat JPG.

**When**

* Citra dianalisis.

**Then**

* Sistem menerima citra dan menjalankan analisis.

**Metode uji:** Boundary Value Analysis.

### AC-08.3 — Timeout

**Given**

* Citra valid tersedia.
* Proses AI membutuhkan **>3,0 detik**.

**When**

* Sistem mencapai batas waktu.

**Then**

* Sistem menampilkan kegagalan/timeout.

**Metode uji:** Performance Test.

---

## US-09 — Confidence Level

### AC-09.1 — Happy Path

**Given**

* Model menghasilkan prediksi.
* Confidence hasil adalah **85%**.

**When**

* Sistem menampilkan hasil.

**Then**

* Sistem menampilkan confidence **85%**.
* Karena **85% ≥70%**, hasil ditampilkan sebagai indikasi dominan.

**Metode uji:** Unit Test + Integration Test.

### AC-09.2 — Boundary 70%

**Given**

* Model menghasilkan confidence tepat **70%**.

**When**

* Hasil ditampilkan.

**Then**

* Confidence ditampilkan sebagai **70%**.
* Status adalah **indikasi dominan**.

**Metode uji:** Boundary Value Analysis.

### AC-09.3 — Boundary 69,99%

**Given**

* Model menghasilkan confidence **69,99%**.

**When**

* Sistem menampilkan hasil.

**Then**

* Confidence ditampilkan.
* Sistem memberikan peringatan **"Hasil Meragukan / Confidence Rendah"**.

**Metode uji:** Boundary Value Analysis.

### AC-09.4 — Timeout

**Given**

* Model belum menghasilkan confidence.
* Waktu inferensi mencapai **>3,0 detik**.

**When**

* Batas waktu terlampaui.

**Then**

* Sistem tidak menampilkan confidence yang tidak berasal dari hasil inferensi.
* Sistem menampilkan timeout/error.

**Metode uji:** Integration + Performance Test.

---

## US-10 — Peringatan Confidence Rendah

### AC-10.1 — Confidence Rendah

**Given**

* Sistem menghasilkan confidence **65%**.

**When**

* Sistem menentukan status hasil.

**Then**

* Sistem menampilkan **"Hasil Meragukan / Confidence Rendah"**.
* Sistem tetap menampilkan confidence **65%**.
* Disclaimer wajib ditampilkan.

**Metode uji:** Integration Test + UAT.

### AC-10.2 — Boundary 70%

**Given**

* Confidence tepat **70%**.

**When**

* Sistem menentukan status.

**Then**

* Sistem **tidak** memberikan status confidence rendah.
* Hasil ditampilkan sebagai indikasi dominan.

**Metode uji:** Boundary Value Analysis.

### AC-10.3 — Timeout

**Given**

* Confidence belum tersedia.
* Inferensi berlangsung **>3,0 detik**.

**When**

* Batas latensi terlampaui.

**Then**

* Sistem menampilkan timeout/error, bukan peringatan confidence rendah.

**Metode uji:** Performance + Negative Test.

---

## US-11 — Indikasi OOD untuk Petani

### AC-11.1 — OOD Berdasarkan Confidence

**Given**

* Sistem memperoleh confidence **45%**.

**When**

* Sistem menentukan status hasil.

**Then**

* Sistem menandai hasil sebagai **indikasi OOD**.
* Sistem tidak menyatakan hasil sebagai klasifikasi yang dapat dipercaya dari 6 kelas target.

**Metode uji:** Integration Test + Boundary Value Analysis.

### AC-11.2 — Boundary 50%

**Given**

* Sistem menghasilkan confidence tepat **50%**.
* Tidak ada indikasi OOD lain.

**When**

* Sistem menentukan status.

**Then**

* Sistem tidak menandai OOD hanya berdasarkan aturan confidence `<50%`.
* Karena **50% <70%**, sistem menampilkan **Hasil Meragukan / Confidence Rendah**.

**Metode uji:** Boundary Value Analysis.

### AC-11.3 — Confidence 49,99%

**Given**

* Sistem menghasilkan confidence **49,99%**.

**When**

* Sistem menentukan status.

**Then**

* Sistem menandai **indikasi OOD** karena confidence **<50%**.

**Metode uji:** Boundary Value Analysis.

### AC-11.4 — Timeout

**Given**

* Sistem belum menghasilkan confidence.
* Inferensi berlangsung **>3,0 detik**.

**When**

* Batas waktu terlampaui.

**Then**

* Sistem menampilkan timeout/error dan tidak menyimpulkan OOD hanya karena tidak adanya confidence.

**Metode uji:** Performance + Negative Test.

---

## US-12 — Indikasi OOD untuk Penyuluh

### AC-12.1 — OOD

**Given**

* Penyuluh memberikan citra yang menghasilkan confidence **40%**.

**When**

* Sistem menyelesaikan inferensi.

**Then**

* Sistem menampilkan indikasi OOD.
* Sistem memperingatkan bahwa objek tidak dapat dipercaya sebagai salah satu dari 6 kelas target.

**Metode uji:** Integration Test.

### AC-12.2 — Boundary 50%

**Given**

* Confidence tepat **50%**.
* Tidak ada indikasi OOD lain.

**When**

* Sistem menentukan status.

**Then**

* Sistem menampilkan **Confidence Rendah**, bukan OOD berdasarkan ambang `<50%`.

**Metode uji:** Boundary Value Analysis.

### AC-12.3 — Timeout

**Given**

* Inferensi membutuhkan **>3,0 detik**.

**When**

* Batas waktu terlampaui.

**Then**

* Sistem menampilkan timeout/error.
* Sistem tidak menghasilkan klaim OOD tanpa hasil analisis.

**Metode uji:** Performance Test.

---

# EPIC 3 — Penyajian Hasil & Transparansi AI

## US-13 — Melihat Hasil Klasifikasi dan Confidence

### AC-13.1 — Happy Path

**Given**

* Citra berhasil dianalisis.
* Prediksi adalah **Tomat Early Blight**.
* Confidence adalah **82%**.
* Waktu inferensi adalah **2,5 detik**.

**When**

* Sistem menyelesaikan analisis.

**Then**

* Sistem menampilkan **Tomat Early Blight**.
* Sistem menampilkan **82%**.
* Sistem menampilkan hasil sebagai indikasi dominan.
* Sistem menampilkan hasil dalam ≤**3,0 detik**.

**Metode uji:** Integration Test + UAT.

### AC-13.2 — Boundary Confidence

**Given**

* Confidence adalah tepat **70%**.

**When**

* Hasil ditampilkan.

**Then**

* Sistem menampilkan confidence **70%**.
* Status adalah indikasi dominan.

**Metode uji:** Boundary Value Analysis.

### AC-13.3 — Timeout

**Given**

* Proses analisis belum selesai.
* Waktu mencapai **3,01 detik**.

**When**

* Sistem melewati batas NFR-07.

**Then**

* Sistem menampilkan timeout/error.
* Sistem tidak menampilkan hasil klasifikasi yang belum tersedia.

**Metode uji:** Performance + Integration Test.

---

## US-14 — Visualisasi Prapemrosesan

### AC-14.1 — Happy Path

**Given**

* Citra valid telah diterima.
* Sistem berhasil melakukan prapemrosesan dan inferensi.

**When**

* Hasil analisis ditampilkan.

**Then**

* Sistem menampilkan visualisasi citra hasil prapemrosesan.
* Visualisasi ditampilkan bersama hasil analisis.

**Metode uji:** Integration Test + UAT.

### AC-14.2 — Citra Boundary 5 MB

**Given**

* Citra JPG berukuran tepat **5 MB**.
* Citra berhasil diproses.

**When**

* Sistem menyelesaikan prapemrosesan.

**Then**

* Visualisasi prapemrosesan tersedia.

**Metode uji:** Boundary + Integration Test.

### AC-14.3 — Timeout

**Given**

* Pemrosesan/inferensi membutuhkan **>3,0 detik**.

**When**

* Batas latensi terlampaui.

**Then**

* Sistem menampilkan timeout/error.
* Sistem tidak menyatakan proses deteksi berhasil.

**Metode uji:** Performance Test.

---

## US-15 — Penafian Hasil AI

### AC-15.1 — Disclaimer pada Confidence Tinggi

**Given**

* Sistem menghasilkan confidence **90%**.
* Hasil termasuk salah satu dari 6 kelas.

**When**

* Sistem menampilkan hasil.

**Then**

* Sistem menampilkan disclaimer:

> **"Hasil AI merupakan indikasi awal, bukan diagnosis definitif dari pakar."**

**Metode uji:** Inspection + UAT.

### AC-15.2 — Disclaimer pada Confidence Rendah

**Given**

* Sistem menghasilkan confidence **60%**.

**When**

* Sistem menampilkan hasil.

**Then**

* Disclaimer tetap ditampilkan.
* Peringatan confidence rendah juga ditampilkan.

**Metode uji:** Integration Test.

### AC-15.3 — Timeout

**Given**

* Inferensi melebihi **3,0 detik**.
* Tidak ada hasil analisis yang berhasil.

**When**

* Sistem menampilkan halaman/error state.

**Then**

* Sistem tidak menampilkan klaim diagnosis.
* Jika tidak ada hasil analisis, tidak boleh ada hasil klasifikasi yang seolah-olah valid.

**Metode uji:** Negative Test.

---

## US-16 — Transparansi untuk Penyuluh

### AC-16.1 — Disclaimer Hasil

**Given**

* Penyuluh menerima hasil klasifikasi dengan confidence **85%**.

**When**

* Hasil ditampilkan.

**Then**

* Sistem menampilkan disclaimer wajib.
* Hasil diposisikan sebagai indikasi awal.

**Metode uji:** UAT + Inspection.

### AC-16.2 — Confidence Rendah

**Given**

* Confidence adalah **65%**.

**When**

* Sistem menampilkan hasil.

**Then**

* Sistem menampilkan peringatan confidence rendah.
* Disclaimer tetap tersedia.

**Metode uji:** Integration Test.

### AC-16.3 — OOD

**Given**

* Confidence adalah **45%**.

**When**

* Sistem menampilkan hasil.

**Then**

* Sistem menampilkan indikasi OOD.
* Sistem tidak memosisikan hasil sebagai diagnosis definitif.

**Metode uji:** Integration Test.

---

# EPIC 4 — Evaluasi & Performa Sistem

## US-17 — Evaluasi Precision, Recall, dan F1-Score 6 Kelas

### AC-17.1 — Evaluasi Lengkap

**Given**

* Dataset evaluasi memiliki sampel untuk seluruh **6 kelas target**.

**When**

* Developer menjalankan evaluasi model.

**Then**

* Sistem/proses evaluasi menghasilkan Precision, Recall, dan F1-Score untuk **6/6 kelas**.

**Metode uji:** Unit Test + Evaluation Test.

### AC-17.2 — Cakupan Kelas

**Given**

* Model hanya menyediakan metrik untuk 5 kelas.

**When**

* Evaluasi dilakukan.

**Then**

* Evaluasi dinyatakan **tidak memenuhi** kebutuhan karena target adalah **6/6 kelas**.

**Metode uji:** Negative Test.

---

## US-18 — Akurasi Dataset Uji

### AC-18.1 — Target Akurasi

**Given**

* Developer menggunakan dataset uji.
* Model diuji terhadap seluruh sampel dataset uji.

**When**

* Akurasi dihitung sebagai:

> prediksi benar ÷ total sampel × 100%.

**Then**

* Sistem/model dinyatakan memenuhi target apabila akurasi **≥91%**.

**Metode uji:** Model Evaluation Test.

### AC-18.2 — Boundary 91%

**Given**

* Akurasi yang diperoleh tepat **91,00%**.

**When**

* Hasil evaluasi diperiksa.

**Then**

* Model dinyatakan **memenuhi benchmark**.

**Metode uji:** Boundary Value Analysis.

### AC-18.3 — Di Bawah Target

**Given**

* Akurasi dataset uji adalah **90,99%**.

**When**

* Evaluasi dilakukan.

**Then**

* Model dinyatakan **tidak memenuhi** target NFR-01.

**Metode uji:** Boundary Value Analysis.

---

## US-19 — Pengujian Real-World

### AC-19.1 — Minimal 60 Sampel

**Given**

* Developer memiliki minimal **60 sampel citra nyata**.

**When**

* Model diuji melalui aplikasi web.

**Then**

* Akurasi real-world dihitung berdasarkan sampel tersebut.
* Target terpenuhi apabila akurasi **≥75%**.

**Metode uji:** System Test + Real-World Evaluation.

### AC-19.2 — Boundary Akurasi 75%

**Given**

* Pengujian dilakukan terhadap tepat **60 sampel**.
* Sebanyak **45 prediksi benar**.

**When**

* Akurasi dihitung.

**Then**

* Akurasi = 45/60 × 100% = **75%**.
* Model dinyatakan memenuhi baseline real-world.

**Metode uji:** Boundary Value Analysis.

### AC-19.3 — Di Bawah Target

**Given**

* Pengujian dilakukan terhadap **60 sampel**.
* Sebanyak **44 prediksi benar**.

**When**

* Akurasi dihitung.

**Then**

* Akurasi = 44/60 × 100% = **73,33%**.
* Model dinyatakan tidak memenuhi baseline **75%**.

**Metode uji:** Evaluation Test.

---

## US-20 — Pemantauan Tomat Late Blight

### AC-20.1 — Recall dan F1 Dipantau

**Given**

* Dataset evaluasi mencakup kelas Tomat Late Blight.

**When**

* Developer menjalankan evaluasi per kelas.

**Then**

* Recall Tomat Late Blight dan F1-Score ditampilkan.
* Nilai dibandingkan dengan baseline **Recall 0,7594** dan **F1-Score 0,8510**.

**Metode uji:** Model Evaluation Test.

### AC-20.2 — Boundary Baseline Recall

**Given**

* Recall Tomat Late Blight = **0,7594**.

**When**

* Developer membandingkan hasil dengan baseline.

**Then**

* Sistem mencatat nilai tersebut sebagai **setara baseline**.

**Metode uji:** Boundary/Regression Test.

### AC-20.3 — Penurunan Performa

**Given**

* Recall Tomat Late Blight = **0,7593**.

**When**

* Developer membandingkan dengan baseline.

**Then**

* Sistem menandai adanya penurunan sebesar **0,0001** dari baseline.

**Metode uji:** Regression Test.

---

## US-21 — Evaluasi Cabai Leaf Curl

### AC-21.1 — Metrik Kelas

**Given**

* Dataset evaluasi mencakup Cabai Leaf Curl.

**When**

* Developer menjalankan evaluasi.

**Then**

* Precision dan Recall Cabai Leaf Curl tersedia.
* Hasil dibandingkan dengan baseline **Precision 0,9711** dan **Recall 0,9619**.

**Metode uji:** Model Evaluation Test.

### AC-21.2 — Boundary Precision

**Given**

* Precision Cabai Leaf Curl = **0,9711**.

**When**

* Developer membandingkan dengan baseline.

**Then**

* Nilai dicatat sebagai **setara baseline**.

**Metode uji:** Boundary/Regression Test.

### AC-21.3 — Pemantauan Error Lapangan

**Given**

* Tersedia data real-world yang mencakup Cabai Leaf Curl.

**When**

* Developer melakukan evaluasi lapangan.

**Then**

* Tingkat kesalahan Cabai Leaf Curl dipantau dan dibandingkan dengan baseline kesalahan **50%**.

**Metode uji:** Real-World Evaluation Test.

---

## US-22 — Evaluasi Early Blight vs Late Blight

### AC-22.1 — Cross-Misclassification

**Given**

* Dataset evaluasi mencakup Tomat Early Blight dan Tomat Late Blight.
* Baseline riset mencatat **14 sampel salah** pada kedua kategori tersebut.

**When**

* Developer melakukan evaluasi klasifikasi.

**Then**

* Kesalahan silang Early Blight ↔ Late Blight dihitung.
* Hasil dibandingkan dengan baseline **14 sampel salah**.

**Metode uji:** Confusion Matrix Analysis + Regression Test.

### AC-22.2 — Boundary Baseline

**Given**

* Jumlah salah klasifikasi silang = **14 sampel**.

**When**

* Developer membandingkan dengan baseline.

**Then**

* Hasil dicatat sebagai **setara baseline**.

**Metode uji:** Boundary/Regression Test.

### AC-22.3 — Penurunan

**Given**

* Jumlah salah klasifikasi silang = **15 sampel**.

**When**

* Developer mengevaluasi hasil.

**Then**

* Sistem mencatat adanya peningkatan kesalahan sebesar **1 sampel** dibandingkan baseline.

**Metode uji:** Regression Test.

---

# Rekapitulasi Coverage Acceptance Criteria

| US    | Fitur                 | Normal | Boundary/Edge | Timeout | Metode Uji                    |
| ----- | --------------------- | :----: | :-----------: | :-----: | ----------------------------- |
| US-01 | Input citra Petani    |    ✓   |       ✓       |    —    | Integration, UAT, BVA         |
| US-02 | Input citra Penyuluh  |    ✓   |       ✓       |    —    | Integration, UAT              |
| US-03 | Panduan Petani        |    ✓   |       —       |    —    | UAT, Inspection               |
| US-04 | Panduan Penyuluh      |    ✓   |       —       |    —    | UAT, Inspection               |
| US-05 | Analisis AI           |    ✓   |       ✓       |    ✓    | Integration, Performance      |
| US-06 | Klasifikasi 6 kelas   |    ✓   |       ✓       |    ✓    | Integration, BVA, Performance |
| US-07 | Analisis AI Penyuluh  |    ✓   |       ✓       |    ✓    | Integration, UAT, Performance |
| US-08 | Analisis AI Pengelola |    ✓   |       ✓       |    ✓    | Integration, UAT, Performance |
| US-09 | Confidence            |    ✓   |       ✓       |    ✓    | Unit, Integration, BVA        |
| US-10 | Confidence rendah     |    ✓   |       ✓       |    ✓    | Integration, BVA              |
| US-11 | OOD Petani            |    ✓   |       ✓       |    ✓    | Integration, BVA              |
| US-12 | OOD Penyuluh          |    ✓   |       ✓       |    ✓    | Integration, BVA              |
| US-13 | Hasil deteksi         |    ✓   |       ✓       |    ✓    | Integration, UAT, Performance |
| US-14 | Preprocessing         |    ✓   |       ✓       |    ✓    | Integration, UAT              |
| US-15 | Disclaimer Petani     |    ✓   |       ✓       |    ✓    | Inspection, Integration       |
| US-16 | Disclaimer Penyuluh   |    ✓   |       ✓       |    —    | UAT, Inspection               |
| US-17 | Metrik 6 kelas        |    ✓   |       ✓       |    —    | Evaluation Test               |
| US-18 | Akurasi dataset       |    ✓   |       ✓       |    —    | Model Evaluation              |
| US-19 | Akurasi real-world    |    ✓   |       ✓       |    —    | System/Evaluation             |
| US-20 | Late Blight           |    ✓   |       ✓       |    —    | Regression/Evaluation         |
| US-21 | Leaf Curl             |    ✓   |       ✓       |    —    | Regression/Evaluation         |
| US-22 | Early vs Late Blight  |    ✓   |       ✓       |    —    | Confusion Matrix/Regression   |

## Parameter QA Utama

Sebagai **baseline pengujian**, seluruh Acceptance Criteria mengacu pada parameter berikut:

| Parameter                                 |             Nilai Wajib |
| ----------------------------------------- | ----------------------: |
| Jumlah kelas target                       |             **6 kelas** |
| Format citra                              |        **JPG/JPEG/PNG** |
| Ukuran maksimum                           |                **5 MB** |
| Confidence tinggi                         |                **≥70%** |
| Confidence rendah                         |                **<70%** |
| OOD berdasarkan confidence                |                **<50%** |
| Latensi inferensi                         |          **≤3,0 detik** |
| Akurasi dataset uji                       |                **≥91%** |
| Sampel real-world minimum                 |            **60 citra** |
| Akurasi real-world                        |                **≥75%** |
| Recall baseline Tomat Late Blight         |              **0,7594** |
| F1 baseline Tomat Late Blight             |              **0,8510** |
| Precision baseline Cabai Leaf Curl        |              **0,9711** |
| Recall baseline Cabai Leaf Curl           |              **0,9619** |
| Error baseline Cabai Leaf Curl            |                 **50%** |
| Error baseline Tomat Normal               |                 **40%** |
| Cross-misclassification Early/Late Blight |           **14 sampel** |
| Disclaimer                                | **100% hasil analisis** |

**Catatan QA penting:** pada aturan yang diberikan, **confidence 50% tepat** belum memenuhi kondisi OOD (`<50%`), tetapi tetap memenuhi kondisi confidence rendah (`<70%`). Sebaliknya, **49,99%** memenuhi kedua kondisi dan harus diprioritaskan sebagai **OOD**. Ini membuat boundary **50% dan 70%** menjadi titik pengujian yang sangat penting.
