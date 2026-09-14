[Peran Integrasi]
Kamu adalah gabungan dari Quality Assurance Lead, Requirements Traceability Analyst, Senior Test Analyst, dan Senior Product Owner/Business Analyst untuk produk digital berfitur AI.

[Tugas Utama]
Berdasarkan seluruh konteks spesifikasi perangkat lunak "AgriScan AI" di bawah ini, susunlah MATRIKS TRACEABILITY KOMPREHENSIF yang menghubungkan kebutuhan secara end-to-end dari tingkat SRS (FR/NFR) hingga ke Acceptance Criteria (Gherkin AC).

================================================================================
[KONTEKS SINTESIS LENGKAP: AGRISCAN AI]
================================================================================

1. Ringkasan Platform & Batasan Riset (MALCOM, 2025):
   - Platform: Website One-Page App (Frontend: HTML/CSS/JS | Backend: Python Flask | Model: CNN TensorFlow/Keras).
   - Scope Klasifikasi Target: Tepat 6 Kelas (Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight).
   - Baseline Kinerja: Akurasi Dataset Uji = 91%; Akurasi Real-World Nyata = 75% (dari 60 sampel uji).
   - Metrik Khusus Evaluasi Developer: 
     * Recall Tomat Late Blight dipantau terhadap baseline 0.7594 (F1-Score 0.8510).
     * Precision & Recall Cabai Leaf Curl dipantau terhadap baseline 0.9711 & 0.9619 (dengan catatan kesalahan uji nyata 50%).
     * Misklasifikasi Tomat Normal dipantau terhadap kesalahan uji nyata 40%.
     * Misklasifikasi silang Tomat Early Blight vs Late Blight (14 sampel salah pada dataset uji).

2. Kebutuhan Fungsional SRS (FR-01 s.d. FR-12):
   - FR-01: Menerima citra tanaman cabai/tomat saat pengguna melakukan pengambilan/pengunggahan → Citra tersedia untuk dianalisis [Must Have | Uji]
   - FR-02: Melakukan analisis citra menggunakan model CNN saat citra valid tersedia → Hasil klasifikasi tanaman [Must Have | Demonstrasi]
   - FR-03: Mengklasifikasikan citra ke dalam 6 kategori target saat analisis selesai → Satu hasil kategori target [Must Have | Uji]
   - FR-04: Menghasilkan confidence level saat model menghasilkan klasifikasi → Nilai confidence (%) pada hasil [Must Have | Uji]
   - FR-05: Menampilkan hasil klasifikasi & confidence level saat analisis selesai → Tampilan informasi hasil deteksi [Must Have | Demonstrasi]
   - FR-06: Menampilkan visualisasi prapemrosesan citra saat citra diproses → Visualisasi citra prapemrosesan [Must Have | Demonstrasi]
   - FR-07: Memberikan peringatan hasil confidence rendah saat confidence berada di kategori rendah (< 70%) → Peringatan kewaspadaan [Should Have | Uji]
   - FR-08: Memberikan indikasi OOD saat citra di luar 6 kelas / confidence sangat rendah (< 50%) → Indikasi objek di luar kategori [Should Have | Uji]
   - FR-09: Menampilkan panduan pengambilan gambar saat pengguna akan memberikan citra → Panduan visual pengambilan citra [Should Have | Demonstrasi]
   - FR-10: Menampilkan informasi bahwa hasil AI adalah indikasi awal saat hasil klasifikasi diberikan → Teks penafian (disclaimer) wajib [Must Have | Inspeksi]
   - FR-11: Mendukung evaluasi 6 kelas target saat evaluasi model dilakukan → Nilai Precision, Recall, F1-Score per kelas [Must Have | Uji]
   - FR-12: Mendukung pengujian menggunakan citra nyata saat evaluasi real-world dilakukan → Evaluasi akurasi real-world (baseline 75%) [Must Have | Uji]

3. Non-Functional Requirements & Aturan Bisnis (NFR & BR):
   - NFR-01: Akurasi dataset uji ≥ 91%.
   - NFR-02: Akurasi real-world ≥ 75% (60 sampel uji).
   - NFR-07: Latensi pemrosesan inferensi AI ≤ 3,0 detik.
   - NFR-08: Pemrosesan citra ringan (Validasi berkas format JPG/PNG, ukuran ≤ 5 MB).
   - NFR-09 & BR-01: Confidence score wajib tampil 100% pada hasil prediksi. Threshold Confidence Tinggi ≥ 70%, Confidence Rendah < 70%.
   - BR-02: Indikasi OOD aktif jika confidence score < 50% atau citra bukan cabai/tomat.
   - BR-03 & NFR-15: 100% hasil wajib menampilkan teks penafian: "Hasil AI merupakan indikasi awal, bukan diagnosis definitif dari pakar."

4. Komponen Teknis & Layanan Model AI yang Terlibat (Aktor Pendukung / Service):
   - Client Browser Validasi (HTML/JS)
   - Image Preprocessing Engine (Python/OpenCV)
   - CNN Model Inference Engine (TensorFlow/Keras 6-class Model)
   - Flask API Gateway / Web Backend
   - Model Evaluation Module & Metrics Calculator (Scikit-Learn Evaluation Suite)

5. Pemetaan User Stories (US-01 s.d. US-22) dan Skenario Acceptance Criteria (AC-01 s.d. AC-22):
   - Epik 1: Penginputan & Panduan Citra (US-01, US-02, US-03, US-04) → AC-01 s.d. AC-04
   - Epik 2: Analisis & Klasifikasi AI (US-05 s.d. US-12) → AC-05 s.d. AC-12
   - Epik 3: Penyajian Hasil & Transparansi AI (US-13 s.d. US-16) → AC-13 s.d. AC-16
   - Epik 4: Evaluasi & Performa Sistem (US-17 s.d. US-22) → AC-17 s.d. AC-22

================================================================================
[FORMAT OUTPUT YANG DIMINTA]
================================================================================

Buatlah **Tabel Matriks Keterlacakan (Traceability Matrix)** terstruktur dengan kolom-kolom berikut:
1. **ID Kebutuhan (SRS)**: ID FR-xx (dan NFR-xx/BR-xx pendukung).
2. **ID User Story**: ID US-xx (sesuai Epik 1–4).
3. **ID Use Case**: ID UC-xx (misal: UC-01 untuk fitur utama atau ID Sub-Use Case terkait).
4. **ID Acceptance Criteria**: ID AC-xx (terdiri dari skenario Happy Flow, Edge Case/Boundary, dan Timeout/Failure).
5. **Komponen Teknis & Model AI Terlibat**: Komponen perangkat lunak / engine AI yang mengeksekusi kebutuhan tersebut.
6. **Rencana & Metode Uji**: Jenis pengujian yang digunakan (misal: Unit Test, Integration Test, End-to-End/UAT Test, Performance/Stress Test, atau Automated Model Evaluation).

================================================================================
[ATURAN PENULISAN KETAT]
================================================================================
- Setiap baris HARUS memiliki keterlacakan lengkap dari FR sampai Acceptance Criteria. Jika terdapat kebutuhan yang belum memiliki turunan lengkap, tandai secara tegas dengan label **[BELUM LENGKAP]** pada kolom terkait.
- DILARANG menyertakan User Flow UI di dalam tabel ini (karena tidak memiliki ID formal).
- DILARANG mengarang data/metrik di luar parameter kuantitatif yang telah ditentukan (Latensi ≤ 3,0s, Berkas ≤ 5MB JPG/PNG, Confidence Threshold 70% dan 50%, Akurasi 91% & 75%, 6 Kelas Target).
- Gunakan Bahasa Indonesia baku, jelas, profesional, dan format tabel Markdown yang rapi dan scannable.