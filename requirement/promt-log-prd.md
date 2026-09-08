[Peran] Kamu adalah requirements analyst senior.
[Tugas] Ubah PRD AgriScan AI berikut menjadi DRAF Software Requirements Specification (SRS) ringkas yang terstruktur dan siap diimplementasikan.

[Konteks]
  PRD hasil revisi :
    ---
    DRAF PRD — AgriScan AI
    Sistem Deteksi Dini Penyakit Tanaman Cabai dan Tomat

    1. Ringkasan Eksekutif
    AgriScan AI adalah prototype aplikasi web satu halaman yang membantu petani, penyuluh pertanian, dan pengelola perkebunan hortikultura melakukan deteksi dini penyakit tanaman cabai dan tomat melalui citra daun/buah. Produk berfokus pada enam kategori: Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, dan Tomat Late Blight. Sistem menggunakan AI berbasis CNN untuk menghasilkan klasifikasi dan skor kepercayaan (confidence level) serta menampilkan visualisasi prapemrosesan citra. Nilai utama produk adalah membantu pengguna memperoleh indikasi awal secara lebih cepat dan konsisten dibandingkan pemeriksaan visual manual, dengan tetap memperhatikan kesenjangan performa lapangan.

    2. Problem Statement & Bukti
    - Problem Statement: Petani dan praktisi pertanian mengalami risiko kerugian hasil panen karena penyakit tanaman cabai dan tomat terlambat terdeteksi secara manual. Sistem berbasis citra membantu deteksi dini, namun performanya di lapangan dapat menurun dibandingkan hasil pengujian dataset.
    - Fakta Riset:
      * 6 kelas target: Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight.
      * Dataset: 3.734 citra (PlantVillage + dataset mandiri).
      * Akurasi latih/validasi: 91% (epoch 18–20); Akurasi dataset uji: 91%.
      * Akurasi pengujian nyata via web: 75% (dari 60 sampel uji) akibat variasi pencahayaan, kualitas/sudut kamera, dan ketiadaan penanganan Out-of-Distribution (OOD).
      * Tingkat kesalahan uji nyata: Cabai Leaf Curl 50%, Tomat Normal 40%.
      * Kemiripan visual: 14 sampel salah antara Tomat Early Blight dan Late Blight pada dataset uji.
      * Evaluasi Metrik: Recall Tomat Late Blight terendah (0.7594, F1 0.8510); Cabai Leaf Curl memiliki Precision 0.9711, Recall 0.9619.
    - Asumsi:
      * [ASUMSI-01] Pengguna memiliki smartphone Android dengan kamera yang memadai.
      * [ASUMSI-02] Pengguna dapat mengakses web app meski koneksi internet terbatas.
      * [ASUMSI-03] Pengguna memahami hasil AI sebagai indikasi awal, bukan diagnosis definitif.
      * [ASUMSI-04] Data pelatihan prototype belum mencakup seluruh variasi lapangan.
      * [ASUMSI-05] Prototype 3 bulan dapat diselesaikan dengan sumber daya yang ada.

    3. Target User & Stakeholder
    - Petani Cabai & Tomat (Pengguna utama - Kebutuhan: Indikasi awal cepat & mudah - Pengaruh: Tinggi)
    - Penyuluh Pertanian Lapangan (Kebutuhan: Alat bantu pemeriksaan lapangan - Pengaruh: Tinggi)
    - Pengelola Perkebunan Hortikultura (Kebutuhan: Pemantauan terstruktur - Pengaruh: Tinggi)
    - Tim Developer Web/AI (Kebutuhan: Pengembangan & perbaikan model - Pengaruh: Tinggi)
    - Peneliti/Pakar Hama (Kebutuhan: Validasi hasil & kategori - Pengaruh: Tinggi)
    - Pengelola Platform/Mitra (Kebutuhan: Keberlanjutan sistem - Pengaruh: Sedang-Tinggi)

    4. Value Proposition
    - Pain yang dikurangi: Keterlambatan deteksi manual, kesulitan membedakan penyakit mirip secara visual, degradasi performa akibat variasi foto, ketidakpastian model AI di lapangan.
    - Gain yang diciptakan: Klasifikasi 6 kelas cepat, confidence level transparan, visualisasi prapemrosesan citra, pemeriksaan konsisten.
    - AI bukan gimmick: AI berfungsi inti menginterpretasikan citra visual, diposisi sebagai alat bantu deteksi dini (bukan pengganti pakar).

    5. Tujuan Produk & KPI Terukur
    - Akurasi dataset uji: ≥ 91% (Cara ukur: Prediksi benar ÷ total sampel uji × 100%)
    - Akurasi pengujian nyata: ≥ 75% baseline (Cara ukur: Prediksi benar ÷ 60 sampel uji nyata × 100%)
    - Confidence level: Tersedia pada 100% hasil prediksi.
    - Cakupan kelas: 6/6 kelas terintegrasi.
    - Evaluasi per kelas: 6/6 kelas dievaluasi Precision, Recall, F1-Score.
    - Waktu pengembangan: ≤ 3 bulan.

    6. Scope Fitur 3 Bulan (MoSCoW)
    - Must Have: Deteksi penyakit berbasis citra (AI★), Confidence level (AI★), Klasifikasi 6 kelas (AI★), Visualisasi prapemrosesan (AI★), Pengambilan/upload citra, Tampilan hasil deteksi.
    - Should Have: Peringatan hasil berkepercayaan rendah (AI★), Penanganan indikasi OOD (AI★), Panduan pengambilan gambar.
    - Could Have: Riwayat hasil deteksi, Informasi ringkas penyakit, Dashboard sederhana.
    - Won't Have: Diagnosis definitif, Rekomendasi pengobatan otomatis, Prediksi hasil panen, Pemantauan seluruh jenis tanaman.

    7. Non-Goals Eksplisit
    Tidak menggantikan pakar, tidak memberi diagnosis definitif, tidak memberi rekomendasi dosis pestisida, tidak mendeteksi penyakit di luar 6 kelas, tidak mendukung tanaman lain, tidak menjamin akurasi lapangan sama dengan dataset, tidak menangani seluruh kasus OOD.

    8. Asumsi & Risiko Utama + Mitigasi
    - Pencahayaan/Sudut/Kamera bervariasi → Panduan pengambilan gambar & evaluasi multi-kondisi.
    - OOD memaksakan klasifikasi → Pengembangan indikasi OOD (Should Have).
    - Early Blight vs Late Blight mirip → Evaluasi khusus & pemantauan F1-score.
    - Recall Late Blight rendah (0.7594) → Jadikan recall Late Blight metrik pantau utama.
    - Error tinggi Cabai Leaf Curl di lapangan (50%) → Pengujian & evaluasi khusus.
    - Internet terbatas → Aplikasi berbasis Web One-Page yang ringan.
    ---

  Acuan kualitas : ISO/IEC 25010 (Pilih karakteristik relevan: Functional Suitability, Performance Efficiency, Usability, Reliability, Security/Privacy).
  Prioritas       : MoSCoW (Must Have, Should Have, Could Have, Won't Have).
  Platform & stack: Website (One-Page App) — Frontend: HTML, CSS, JavaScript | Backend: Python, Flask | AI Model: CNN (TensorFlow/Keras).

[Format output]
  1) Tujuan, Scope, dan Definisi Istilah;
  2) User & Stakeholder, Lingkungan Operasi, Asumsi & Dependensi;
  3) Functional Requirements (FR): Tabel FR-01..FR-n 
     - Gunakan pola wajib: "Sistem harus dapat <aksi> <objek> saat <kondisi> → <output>"
     - Kolom tabel: ID FR | Deskripsi Kebutuhan (Pola) | Prioritas MoSCoW | Metode Verifikasi (Uji/Inspeksi/Demonstrasi)
  4) Non-Functional Requirements (NFR): Tabel NFR-01..NFR-m
     - Kolom tabel: ID NFR | Kategori ISO/IEC 25010 | Metrik & Target | Kondisi Pengukuran
     - Wajib mencakup: Akurasi AI (Dataset Uji ≥91%, Real-World ≥75%), Latensi AI, Keamanan, Privasi, Usability.
  5) Kebutuhan Data Minimum Fitur AI (Input Citra → Preprocessing → Model Output);
  6) Aturan Bisnis Hasil Riset (Business Rules terkait ambang batas confidence, penanganan OOD, & batas klaim AI);
  7) Matriks Traceability: Pemetaan FR/NFR ke Fitur PRD / Bukti Riset Terkait.

[Aturan]
  - Setiap FR/NFR harus dapat ditelusuri secara ketat ke bukti pada PRD/riset; DILARANG menambah kebutuhan di luar konteks.
  - HENTIKAN pembahasan jika mulai masuk ke detail arsitektur teknis/UI design (fokus penuh pada Functional & Non-Functional Requirements).
  - Gunakan Bahasa Indonesia baku dan format Markdown yang rapi.s