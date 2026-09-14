[Peran Integrasi]
Kamu adalah gabungan dari Senior QA Engineer, Test Analyst, dan Senior Product Owner/Business Analyst untuk produk digital berbasis AI.

[Tugas Utama]
Berdasarkan spesifikasi SRS, Aturan Bisnis, dan User Stories "AgriScan AI" di bawah ini, susunlah:
1. DRAFT Use Case Detail (UC-01) beserta Skenario Utama (Happy Flow) dan Skenario Eksepsi.
2. DRAFT Acceptance Criteria (Format Gherkin: Given-When-Then) secara komprehensif untuk seluruh User Stories yang ada, dengan keterukuran angka yang pasti.

================================================================================
[KONTEKS SINTESIS: AGRISCAN AI]
================================================================================

1. Spesifikasi Teknis & Parametrik SRS/NFR:
   - Scope Klasifikasi Target: Tepat 6 kelas (Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight).
   - NFR-01 (Akurasi Uji Dataset): Benchmark ≥ 91%.
   - NFR-02 (Akurasi Lapangan/Real-World): Baseline ≥ 75% dari minimal 60 sampel citra nyata.
   - NFR-07 (Latensi AI): Waktu inferensi model AI hingga hasil keluar maksimal ≤ 3,0 detik.
   - NFR-08 & Validasi Berkas: Format berkas wajib JPG/JPEG atau PNG dengan ukuran maksimal ≤ 5 MB.
   - NFR-09 & BR-01 (Confidence Level): Skor kepercayaan wajib tampil pada 100% hasil prediksi.
     * High Confidence: Confidence Level ≥ 70% (Tampil sebagai indikasi dominan).
     * Low Confidence / Doubtful (BR-01, BR-03): Confidence Level < 70% (Wajib menampilkan peringatan hasil meragukan).
   - BR-02 (Penanganan OOD - Out-of-Distribution): Jika citra di luar 6 kelas target atau confidence score < 50%, sistem memberikan peringatan indikasi OOD (objek tidak dikenali/di luar kategori).
   - BR-03 & FR-10 (Penafian/Disclaimer Wajib): 100% hasil analisis WAJIB menyertakan teks penafian: "Hasil AI merupakan indikasi awal, bukan diagnosis definitif dari pakar."
   - BR-05 (Metrik Khusus Evaluasi Developer): 
     * Recall Tomat Late Blight dipantau terhadap baseline 0.7594 (F1-Score 0.8510).
     * Precision & Recall Cabai Leaf Curl dipantau terhadap baseline 0.9711 & 0.9619 (dengan perhatian pada tingkat kesalahan uji nyata 50%).
     * Misklasifikasi Tomat Normal dipantau terhadap baseline kesalahan 40%.
     * Cross-misclassification Tomat Early Blight vs Late Blight dipantau terhadap 14 sampel salah pada dataset uji.

2. Daftar Epik & User Stories Terintegrasi:
   - Epik 1: Penginputan & Panduan Citra (US-01, US-02, US-03, US-04)
   - Epik 2: Analisis & Klasifikasi AI (US-05, US-06, US-07, US-08, US-09, US-10, US-11, US-12)
   - Epik 3: Penyajian Hasil & Transparansi AI (US-13, US-14, US-15, US-16)
   - Epik 4: Evaluasi & Performa Sistem (US-17, US-18, US-19, US-20, US-21, US-22)

================================================================================
[FORMAT OUTPUT YANG DIMINTA]
================================================================================

BAGIAN 1: USE CASE DETAIL (Fitur Inti Must Have: US-01, US-05, US-06, US-09, US-13, US-14, US-15)
- ID Use Case  : UC-01
- Nama Use Case: Deteksi Dini Penyakit Tanaman Cabai dan Tomat
- Aktor Utama  : Petani / Penyuluh Pertanian
- Pre-kondisi  : Pengguna mengakses aplikasi web AgriScan AI via browser smartphone/PC; Berkas citra tanaman berformat JPG/PNG (≤ 5MB) siap diunggah atau diambil via kamera.
- Post-kondisi : Sistem menampilkan hasil klasifikasi (dari 6 kelas target), skor confidence level (%), visualisasi prapemrosesan citra, dan penafian wajib "indikasi awal".
- Skenario Utama (Happy Flow): Terurut langkah demi langkah secara sistematis dari aksi aktor hingga respons sistem (termasuk batas latensi ≤ 3,0 detik).
- Skenario Alternatif / Eksepsi: 
  * Format/Ukuran berkas tidak valid (> 5 MB / Non-JPG/PNG).
  * Confidence level rendah (< 70%).
  * Indikasi objek OOD (< 50% / di luar 6 kelas).
  * Kegagalan koneksi/server Flask timeout (> 3,0 detik).

BAGIAN 2: ACCEPTANCE CRITERIA BERPOLA GHERKIN (QA/Test Analyst)
Buat kriteria penerimaan terukur (Given-When-Then) untuk tiap User Story (US-01 s.d. US-22).

Khusus untuk User Story berlabel Fitur AI ★ (US-05, US-06, US-07, US-08, US-09, US-10, US-11, US-12, US-13, US-14), WAJIB mencakup:
1. Skenario Normal (Happy Path)
2. Skenario Data Masukan Batas (Edge Case / Boundary Value)
3. Skenario Kegagalan Respons / Timeout Limit (NFR-07)
4. Usulan Metode Uji yang direkomendasikan (misal: Unit Test, Integration Test, atau User Acceptance Test/UAT).

[ATURAN PENULISAN]
- DILARANG menggunakan kata-kata samar tanpa patokan (misal: "harus cepat", "harus akurat").
- WAJIB menggunakan parameter kuantitatif yang presisi (latensi ≤ 3,0 detik, confidence threshold 70%, ukuran berkas ≤ 5 MB, 6 kelas target, baseline akurasi 91% dan 75%).
- Bahasa Indonesia baku, jelas, profesional, dan format Markdown yang rapi.