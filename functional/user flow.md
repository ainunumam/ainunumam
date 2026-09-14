[Peran Integrasi]
Kamu adalah gabungan dari UX Designer, Interaction Analyst, dan Senior QA/Business Analyst untuk produk digital cerdas berfitur AI.

[Tugas Utama]
Berdasarkan data riset dan spesifikasi produk "AgriScan AI" di bawah ini, susunlah:
1. DRAFT User Flow terstruktur (termasuk status sistem dan diagram Mermaid/teks).
2. DRAFT Use Case Detail (UC-01) beserta Acceptance Criteria terukur berbasis Given-When-Then.

================================================================================
[KONTEKS SINTESIS: AGRISCAN AI]
================================================================================

1. Persona & Skenario Singkat:
   - Persona: Pak Budi (45 tahun), petani cabai dan tomat yang menggunakan smartphone Android di area perkebunan dengan koneksi internet terbatas.
   - Skenario: Pak Budi menemukan daun tanaman tomatnya menunjukkan gejala bercak kecokelatan. Ia membuka aplikasi web AgriScan AI via browser ponsel, mengambil foto daun secara langsung di lapangan, lalu menunggu sistem menganalisis untuk mendapatkan indikasi awal penyakit dan tingkat keyakinan (confidence level).

2. Keterbatasan & Performa Sistem Berdasarkan Riset (MALCOM, 2025):
   - Scope Kategori AI: 6 Kelas Target (Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight).
   - Metrik AI: Benchmark Uji Dataset = 91%; Baseline Lapangan Nyata = 75% (dari 60 sampel uji).
   - Problem Khusus: Resiko tinggi misklasifikasi pada Cabai Leaf Curl (error 50%), Tomat Normal (error 40%), serta kemiripan visual Tomat Early Blight vs Late Blight (14 sampel tertukar).
   - Metrik Kunci: Recall Tomat Late Blight terendah (0.7594, F1 0.8510); Precision Cabai Leaf Curl tinggi (0.9711).

3. Parameter NFR & Baturan Bisnis (SRS/NFR):
   - NFR-07 (Latensi Pemrosesan AI): Waktu respons inferensi AI hingga hasil keluar maksimal ≤ 3,0 detik pada jaringan internet standar/terbatas.
   - NFR-08 (Kualitas & Validasi Citra): Input citra harus berformat JPG/PNG dengan ukuran berkas maksimal 5 MB.
   - BR-01 (Ambang Batas Confidence Tinggi): Jika Confidence Level ≥ 70%, hasil klasifikasi ditampilkan sebagai indikasi dominan.
   - BR-02 (Ambang Batas Confidence Rendah / Doubtful): Jika Confidence Level < 70%, sistem wajib menampilkan peringatan "Hasil Meragukan / Confidence Rendah".
   - BR-03 (Penanganan OOD - Out-of-Distribution): Jika fitur citra di luar 6 kelas target atau confidence score amat sangat rendah (< 50%), sistem menandai indikasi OOD (bukan dari 6 kelas target).
   - BR-04 (Penafian/Disclaimer Wajib): 100% hasil analisis WAJIB menyertakan label/penafian: "Hasil AI merupakan indikasi awal, bukan diagnosis definitif dari pakar."

4. Daftar User Stories Terkait (Epik 1 - 3):
   - US-01 & US-02: Pengambilan/pengunggahan citra tanaman (Must Have).
   - US-05 & US-06: Analisis AI & Klasifikasi ke dalam 6 kelas target (Must Have).
   - US-09 & US-13: Menampilkan hasil klasifikasi dan confidence level (Must Have).
   - US-10 & US-11: Peringatan confidence rendah & penanganan objek OOD (Should Have).
   - US-14: Menampilkan visualisasi prapemrosesan citra (Must Have).
   - US-15 & US-16: Penafian bahwa hasil AI adalah indikasi awal (Must Have).

================================================================================
[FORMAT OUTPUT YANG DIMINTA]
================================================================================

BAGIAN 1: USER FLOW (Perspektif UX & Interaction Analyst)
1. Langkah Alur Pengguna: Dari titik masuk (landing page web), validasi input, pemrosesan backend/AI, hingga penyajian hasil.
2. Penanganan 4 Status Sistem Eksplisit:
   - Validasi Awal di Perangkat (Client-Side Validation): Pengecekan ukuran file (max 5MB) dan ekstensi file (JPG/PNG).
   - Indikator Proses (Loading State): Umpan balik visual saat inferensi AI berlangsung (toleransi latensi ≤ 3,0 detik sesuai NFR-07).
   - Penanganan Hasil Analisis (Conditional State):
     * High Confidence (≥ 70%): Tampilan hasil yakin + confidence level.
     * Low Confidence (< 70% / OOD): Tampilan peringatan hasil meragukan / indikasi objek di luar 6 kelas target.
   - Jalur Cadangan (Fallback State): Antisipasi kegagalan server Flask / timeout / AI crash (menampilkan pesan error ramah pengguna + tombol coba lagi).
3. Diagram Alur: Gunakan format sintaks kode **Mermaid** (graph TD/flowchart) yang rapi dan mudah dibaca.
4. Tabel Matriks Traceability Alur: Pemetaan alur ke Use Case / User Story terkait.

BAGIAN 2: USE CASE DETAIL & ACCEPTANCE CRITERIA (Perspektif QA / BA Senior)
1. Use Case Detail:
   - ID Use Case  : UC-01
   - Nama Use Case: Deteksi Dini Penyakit Tanaman Cabai dan Tomat Berbasis Citra
   - Aktor Utama  : Petani / Penyuluh Pertanian Lapangan
   - Pre-kondisi  : Pengguna mengakses web app AgriScan AI via browser smartphone/PC; Kamera atau file citra tanaman siap digunakan.
   - Post-kondisi : Sistem menampilkan hasil klasifikasi 6 kelas, skor confidence level (%), visualisasi citra prapemrosesan, serta label penafian "indikasi awal".
   - Skenario Utama (Happy Flow): Terurut secara teknologis dari nomor 1..n dari aksi aktor hingga respons sistem.
   - Skenario Alternatif / Eksepsi: Penanganan file invalid, confidence rendah, indikasi OOD, dan server error.

2. Acceptance Criteria (Minimal 3 Skenario Konkret dengan Format Given-When-Then):
   - Skenario 1: Sukses - Deteksi Tanaman dengan Confidence Tinggi (Happy Flow, Latensi ≤ 3s, Confidence ≥ 70%, 6 Kelas Target, Visualisasi Preprocessing, Penafian Wajib).
   - Skenario 2: Peringatan - Penanganan Citra Ber-confidence Rendah / Indikasi OOD (Confidence < 70% atau Objek Tidak Dikenali).
   - Skenario 3: Gagal - Validasi Input Berkas Tidak Sesuai Ketentuan (File > 5MB atau Format Non-JPG/PNG).

[ATURAN PENULISAN]
- Parameter angka (latensi 3 detik, confidence 70%, max 5MB, 6 kelas) HARUS dimasukkan ke dalam skenario QA secara kuantitatif.
- Gunakan Bahasa Indonesia baku, jelas, profesional, dan format Markdown yang rapi.
- DILARANG menyimpang dari batasan 6 kelas target yang telah ditentukan pada riset.
