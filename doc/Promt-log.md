[Peran]
Kamu adalah Senior Software Architect untuk aplikasi Mobile/Web berbasis AI.

[Tugas]
Buatlah DRAF HIGH-LEVEL DESIGN (HLD) teknis berdasarkan keseluruhan dokumen PRD, SRS, dan User Stories dari proyek "AgriScan AI" yang dilampirkan di bawah ini.

[Konteks & Stack Usulan]
- Platform: Website One-Page App (Mobile-friendly PWA)
- Stack Usulan: Frontend (React.js / Vite + Tailwind CSS), Backend API (Python FastAPI), AI Inference Service (ONNX Runtime CPU / PyTorch), Data Store (SQLite / PostgreSQL & Object Storage lokal/S3)
- Konstrain utama: Prototype 1 semester (3 bulan), 1 fitur AI inti, biaya infrastruktur minimal (Free tier / Low-cost VPS).

--------------------------------------------------------------------------------
DOKUMEN MASUKAN (PRD, SRS, USER STORIES)
--------------------------------------------------------------------------------

--- DRAF PRD ---
1. Ringkasan Eksekutif:
AgriScan AI adalah prototype aplikasi web satu halaman untuk deteksi dini penyakit tanaman cabai dan tomat melalui citra daun/buah berbasis AI CNN.
Target 6 Kategori: Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight.
Fitur utama: Klasifikasi, Confidence Level (skor kepercayaan), dan Visualisasi Prapemrosesan Citra.
Tantangan: Akurasi dataset 91%, namun akurasi pengujian nyata turun menjadi 75% akibat pencahayaan, sudut/kualitas kamera, dan ketiadaan mekanisme Out-Of-Distribution (OOD).

2. Problem Statement & Bukti Riset:
- Cabai Leaf Curl: Kesalahan pengujian nyata mencapai 50%.
- Tomat Normal: Kesalahan pengujian nyata mencapai 40%.
- Early Blight vs Late Blight: Memiliki kemiripan visual (14 sampel salah pada dataset uji).
- Recall Tomat Late Blight: Terendah (0,7594; F1-Score 0,8510).
- Precision & Recall Cabai Leaf Curl: 0,9711 & 0,9619.

3. Asumsi PRD:
[ASUMSI-01] Pengguna memiliki smartphone Android dengan kamera yang memadai.
[ASUMSI-02] Pengguna dapat mengakses web app meskipun koneksi internet terbatas.
[ASUMSI-03] Hasil AI merupakan indikasi awal, bukan diagnosis definitif.
[ASUMSI-04] Data prototype belum mencakup seluruh variasi kondisi lapangan.
[ASUMSI-05] Pengujian prototype selama 3 bulan dapat dilakukan dengan sumber daya yang ada.

4. Scope Fitur MoSCoW (3 Bulan):
- Must Have: Deteksi penyakit citra (6 kelas), Confidence level, Visualisasi prapemrosesan, Pengambilan/upload citra, Tampilan hasil deteksi.
- Should Have: Peringatan confidence rendah, Indikasi OOD (Out-Of-Distribution), Panduan pengambilan gambar.
- Could Have: Riwayat hasil deteksi, Informasi ringkas penyakit, Dashboard sederhana.
- Won't Have: Diagnosis definitif, Rekomendasi pengobatan/pestisida otomatis, Prediksi hasil panen, Pemantauan tanaman lain.

--- DRAF SRS ---
1. Functional Requirements (FR):
- FR-01: Menerima citra tanaman cabai/tomat (Upload/Kamera).
- FR-02: Menganalisis citra menggunakan model CNN.
- FR-03: Mengklasifikasikan ke dalam 6 kelas target.
- FR-04: Menghasilkan confidence level pada setiap prediksi.
- FR-05: Menampilkan hasil klasifikasi & confidence level.
- FR-06: Menampilkan visualisasi prapemrosesan citra.
- FR-07: Memberikan peringatan untuk hasil confidence rendah.
- FR-08: Memberikan indikasi citra berpotensi OOD.
- FR-09: Menampilkan panduan pengambilan gambar.
- FR-10: Menampilkan disclaimer bahwa hasil AI adalah indikasi awal.
- FR-11: Mendukung evaluasi metrik (Precision, Recall, F1) untuk 6 kelas.
- FR-12: Mendukung pengujian menggunakan citra nyata (minimal 60 sampel).

2. Non-Functional Requirements (NFR) & Business Rules (BR):
- NFR-01/02: Target Akurasi Dataset Uji ≥91%, Real-World Test ≥75%.
- NFR-07/08: Pemrosesan & latensi AI harus cukup ringan untuk pemeriksaan lapangan [ASUMSI-NFR-01].
- NFR-09: Confidence level tersedia pada 100% hasil prediksi.
- NFR-13/14: Privacy & Security: Tidak mengungkapkan data pengguna tidak perlu, citra hanya untuk analisis [ASUMSI-NFR-02, ASUMSI-NFR-03].
- BR-01: Ambang confidence rendah harus divalidasi sebelum implementasi [ASUMSI-BR-01].
- BR-02: Indikasi OOD untuk mengurangi salah klasifikasi objek luar target [ASUMSI-BR-02].
- BR-03: Batas Klaim AI (Indikasi awal, bukan diagnosis definitif).

--- USER STORIES (RINGKASAN EPIK) ---
- Epik 1 (Penginputan & Panduan): US-01 s.d. US-04 (Upload/Capture Citra & Panduan Foto).
- Epik 2 (Analisis & Klasifikasi AI): US-05 s.d. US-12 (Analisis CNN, 6 Kelas, Confidence Score, Peringatan Low Confidence, Indikasi OOD).
- Epik 3 (Penyajian Hasil & Transparansi): US-13 s.d. US-16 (Tampilan Hasil, Visualisasi Preprocessing, Disclaimer Indikasi Awal).
- Epik 4 (Evaluasi & Performa): US-17 s.d. US-22 (Logging & Evaluasi 6 Kelas, Monitoring Late Blight & Leaf Curl).

--------------------------------------------------------------------------------
FORMAT OUTPUT HLD YANG HARUS DIGENERASI
--------------------------------------------------------------------------------
Tolong susun draf HLD dengan format output sebagai berikut:

1) Diagram Arsitektur (Menggunakan Mermaid Syntax):
   Client (Browser/PWA) → Backend API → AI Service → Data Store.
2) Deskripsi Komponen & Decision Matrix:
   - Jelaskan peran, tanggung jawab, dan usulan teknologi tiap komponen.
   - Sertakan TABEL TRADE-OFF Penempatan AI (On-Device Client vs Cloud API) yang mengevaluasi: Akurasi, Latensi, Biaya, Privasi, Effort, lalu berikan rekomendasi final beserta alasannya.
3) Aliran Data End-to-End Fitur AI:
   Alur: Input → Preprocessing → Inference → Postprocessing/Validation (Confidence & OOD) → Output → Storage.
   Sertakan skenario handling & titik fallback saat model gagal / confidence rendah / OOD.
4) Kontrak Antarkomponen Tingkat Tinggi:
   Spesifikasi REST API utama (`POST /api/v1/detect`), format JSON Request & Response (Skenario Normal & Skenario Low-Confidence/OOD).
5) Security & Privacy by Design:
   Penerapan Auth/Rate limiting, enkripsi, penanganan data sensitif/EXIF, dan logging.
6) Lingkungan Deployment Ringkas:
   Arsitektur deployment untuk Development, Staging, dan Production (fokus pada biaya minimal).

[Aturan Penulisan]
- Desain HANYA berdasarkan FR/NFR/BR yang ada. Jika ada gap arsitektural, tandai dengan tag `[ASUMSI-XX]`.
- JANGAN masuk ke detail level kelas, method, atau DDL query database (karena itu bagian LLD).
- Setiap keputusan besar harus disertai alasan singkat (1-2 kalimat) + alternatifnya.

[Peran]
Kamu adalah Software Engineer Senior (sesuai stack Fastapi/React).

[Tugas]
Buat DRAF LOW-LEVEL DESIGN (LLD) untuk fitur prioritas MUST pada SRS dan HLD AgriScan AI yang dilampirkan di bawah ini.

[Konteks & Stack Tim]
- Platform: Website One-Page App / PWA Mobile-friendly
- Stack: Frontend (React + Vite + Tailwind CSS), Backend (Python FastAPI), AI Inference (ONNX Runtime CPU), Database (SQLite/PostgreSQL dengan SQLAlchemy ORM)
- Arsitektur & Pola: Clean Architecture / Layered Architecture (Presentation -> Application -> Domain -> Infrastructure)
- Konstrain: Prototype 1 semester (3 bulan), 1 fitur AI inti, biaya minimal.

[Output yang Diminta]
1) Desain Modul/Class (Fitur Must + AI):
   - Buat rancangan class/module untuk 2-3 fitur Must terpenting (Image Analysis, Preprocessing, Detection Result).
   - Cantumkan: Tanggung jawab, atribut kunci (dengan tipe data), dan method utama (parameter + return type).
2) Skema Data:
   - Buat skema entitas database (SQLAlchemy Model / DDL SQL / ERD Teks).
   - Sertakan tabel untuk logging prediksi, metadata evaluasi real-world test (60 sampel), dan metrik per kelas.
   - Cantumkan primary key, foreign key, data types, dan constraints.
3) Spesifikasi API Detail Endpoint Inti:
   - Path: `POST /api/v1/detect`
   - Method, Headers, Query/Body Request (multipart/form-data).
   - Response JSON lengkap untuk 3 Skenario: Normal (High Confidence), Low Confidence Warning, dan Potential OOD.
   - Daftar Kode Error HTTP & Internal Error Code (misal: `INVALID_IMAGE_FORMAT`, `MODEL_TIMEOUT`, `OOD_DETECTED`).
4) Sequence Diagram / Alur Detail Fitur AI (Teks / PlantUML / Mermaid):
   - Alur detail: Validasi Input -> Preprocessing -> Model Inference (ONNX) -> Postprocessing -> Storage Logging -> Response.
   - Sertakan penanganan eksplisit untuk timeout (misal: > 5 detik) dan kegagalan model.
5) Rancangan Error Handling & Fallback:
   - Strategi Retry/Timeout, Pembuatan Pesan Error Ramah Pengguna (bahasa non-teknis untuk petani), dan Penanganan Mode Koneksi Lambat/Offline.
6) Tabel Traceability:
   - Pemetaan elemen LLD (Class, Endpoint, Table) ke ID FR/NFR/BR pada SRS.

[Aturan]
- Turunkan murni dari SRS dan HLD; DILARANG menambah fitur di luar requirement.
- Jika ada pilihan library/algoritma yang belum ditentukan di HLD, berikan 2 Opsi + Kriteria Pilih, lalu tulis tag `[KEPUTUSAN TIM: ...]` yang wajib diisi tim.
- Nama Class/Field/Variable menggunakan Bahasa Inggris; penjelasan teks menggunakan Bahasa Indonesia.

--------------------------------------------------------------------------------
DOKUMEN MASUKAN (SRS & HLD REVISI)
--------------------------------------------------------------------------------

--- DRAF SRS ---
Tujuan: Indikasi awal penyakit cabai dan tomat berbasis citra CNN (6 kelas).
6 Kelas Output: Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight.
Priority Must Have:
- FR-01: Menerima citra tanaman (Upload/Capture).
- FR-02: Analisis citra dengan model CNN.
- FR-03: Klasifikasi ke 6 kelas target.
- FR-04: Menghasilkan confidence level (100% dari hasil prediksi).
- FR-05: Tampilan hasil deteksi & confidence level.
- FR-06: Visualisasi prapemrosesan citra.
- FR-10: Penampilan disclaimer bahwa hasil AI adalah indikasi awal.
- FR-11: Support evaluasi 6 kelas (Precision, Recall, F1).
- FR-12: Support real-world testing (minimal 60 sampel).
Priority Should Have:
- FR-07: Peringatan confidence rendah.
- FR-08: Indikasi citra Out-Of-Distribution (OOD).
- FR-09: Panduan pengambilan gambar.
Key NFRs & BRs:
- NFR-01/02: Akurasi Dataset Uji ≥91%, Real-World Test ≥75%.
- NFR-07/08: Latensi AI rendah & pemrosesan citra ringan.
- BR-01: Threshold confidence rendah (misal <70% warn, <50% OOD/invalid) perlu disesuaikan.
- BR-02: Indikasi OOD untuk cegah salah klasifikasi objek luar target.
- BR-03: Batas Klaim AI (bukan diagnosis definitif).

--- DRAF HLD ---
Arsitektur: PWA Client (React/Vite) -> REST API (FastAPI) -> AI Inference (ONNX Runtime CPU) -> Data Store (SQLite/PostgreSQL) + Local Object Storage.
Decision Matrix: Server-side AI Inference (Cloud API) dipillih untuk menjaga konsistensi preprocessing & model.

Endpoint Inti: `POST /api/v1/detect`
Thresholding Logika Postprocessing:
- Confidence ≥ 70%: HIGH_CONFIDENCE (Indikasi Dominan)
- 50% ≤ Confidence < 70%: LOW_CONFIDENCE (Hasil Meragukan / Warn)
- Confidence < 50% atau Out-of-Domain: POTENTIAL_OOD

Data Flow & Fallback:
1. Input Capture/Upload (Client limit ≤5MB, JPG/PNG).
2. Client validation -> Backend validation (MIME, Decode).
3. Preprocessing (Resize/Normalization tensor) & Generasi Citra Visualisasi Preprocessing.
4. Model Inference via ONNX Runtime CPU.
5. Postprocessing (Calculate Confidence & OOD threshold).
6. Response JSON ke Client & Logging Async ke DB/Storage.
7. Fallback: Model error/Timeout -> Return HTTP 503 dengan pesan error ramah pengguna tanpa menampilkan prediksi palsu.
Security & Privacy: HTTPS TLS 1.3, Strip EXIF metadata sebelum simpan, Rate limiting per IP, Logging anonymized.