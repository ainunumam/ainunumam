# DRAF Use Case & Acceptance Criteria — AgriScan AI

> **Catatan QA:** SRS belum menetapkan angka untuk **ambang confidence rendah** dan **target latensi AI**. Karena Acceptance Criteria wajib terukur, angka berikut ditandai sebagai **[ASUMSI]** dan perlu divalidasi sebelum SRS/AC ditetapkan sebagai baseline final.

---

# 1. Use Case Detail

## UC-01 — Deteksi Dini Penyakit Tanaman Cabai dan Tomat

| Elemen                   | Detail                                                                                                                                                                        |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ID Use Case**          | **UC-01**                                                                                                                                                                     |
| **Nama Use Case**        | **Deteksi Dini Penyakit Tanaman Cabai dan Tomat**                                                                                                                             |
| **Aktor Utama**          | Petani / Penyuluh Pertanian                                                                                                                                                   |
| **Tujuan**               | Memperoleh indikasi awal kondisi tanaman cabai atau tomat berdasarkan citra menggunakan AI                                                                                    |
| **Pre-kondisi**          | 1. Pengguna mengakses aplikasi web AgriScan AI melalui browser smartphone/PC. 2. Kamera atau file citra tanaman siap digunakan. 3. Citra merupakan objek yang akan diperiksa. |
| **Post-kondisi**         | Sistem menampilkan hasil klasifikasi dari **6 kelas target**, confidence level, visualisasi citra prapemrosesan, serta penafian bahwa hasil AI merupakan **"indikasi awal"**. |
| **Prioritas**            | Must Have                                                                                                                                                                     |
| **User Stories terkait** | US-01, US-05, US-06, US-09, US-13, US-14, US-15                                                                                                                               |
| **FR terkait**           | FR-01, FR-02, FR-03, FR-04, FR-05, FR-06, FR-10                                                                                                                               |
| **NFR terkait**          | NFR-01, NFR-02, NFR-03, NFR-07, NFR-08, NFR-09, NFR-11, NFR-15                                                                                                                |
| **Business Rules**       | BR-01, BR-03, BR-04                                                                                                                                                           |

## 1.1 Batas Klasifikasi

Sistem hanya memberikan klasifikasi pada **enam kelas target** berikut:

1. Cabai Normal
2. Cabai Antraknosa
3. Cabai Leaf Curl
4. Tomat Normal
5. Tomat Early Blight
6. Tomat Late Blight

Sistem **tidak boleh mengklaim diagnosis definitif** berdasarkan hasil klasifikasi.

---

## 1.2 Skenario Utama — Happy Flow

| Langkah | Aktor                                                                   | Sistem                                                                                          |
| ------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **1**   | Pengguna membuka AgriScan AI melalui browser.                           | Sistem menampilkan fungsi untuk memberikan citra tanaman.                                       |
| **2**   | Pengguna mengambil foto melalui kamera atau memilih file citra tanaman. | Sistem menerima citra untuk proses analisis.                                                    |
| **3**   | Pengguna mengirimkan citra untuk dianalisis.                            | Sistem memproses citra melalui tahap prapemrosesan.                                             |
| **4**   | —                                                                       | Sistem menampilkan visualisasi citra hasil prapemrosesan.                                       |
| **5**   | —                                                                       | Sistem melakukan klasifikasi citra menggunakan model CNN.                                       |
| **6**   | —                                                                       | Sistem menghasilkan satu kategori dari enam kelas target beserta confidence level.              |
| **7**   | —                                                                       | Sistem menampilkan kategori hasil klasifikasi dan confidence level kepada pengguna.             |
| **8**   | —                                                                       | Sistem menampilkan penafian bahwa hasil merupakan **indikasi awal**, bukan diagnosis definitif. |
| **9**   | Pengguna membaca hasil.                                                 | Proses deteksi selesai.                                                                         |

### Contoh Happy Flow

Misalnya pengguna memasukkan foto daun cabai dan model menghasilkan:

> **Hasil: Cabai Antraknosa**
> **Confidence: 94%**
> **Status: Indikasi awal**

Hasil tersebut memenuhi cakupan enam kelas dan confidence berada di atas ambang tinggi **[ASUMSI-AC-01: ≥80%]**.

---

# 2. Acceptance Criteria

## Skenario 1 — Sukses: Deteksi Tanaman dengan Confidence Tinggi

### AC-01 — Deteksi berhasil dengan confidence tinggi

**Given**

* Pengguna telah membuka AgriScan AI.
* Pengguna memberikan citra tanaman cabai atau tomat yang dapat diproses.
* Citra termasuk objek yang sesuai dengan salah satu dari **6 kelas target**.
* **[ASUMSI-AC-01]** Ambang confidence tinggi ditetapkan sebesar **≥80%**.
* **[ASUMSI-AC-02]** Target latensi pemrosesan AI ditetapkan **≤5 detik** sejak citra siap dianalisis sampai hasil klasifikasi tersedia.

**When**

* Pengguna mengirimkan citra untuk dianalisis.

**Then**

* Sistem menerima citra dan melakukan proses analisis.
* Sistem menghasilkan **tepat satu** klasifikasi dari 6 kelas target.
* Sistem menampilkan confidence level **≥80%**.
* Sistem menampilkan visualisasi citra hasil prapemrosesan.
* Sistem menampilkan hasil klasifikasi dan confidence level.
* Sistem menampilkan penafian **"indikasi awal"**.
* Hasil klasifikasi tersedia dalam waktu **≤5 detik [ASUMSI-AC-02]**.

**Contoh hasil yang valid:**

| Parameter                 | Hasil            |
| ------------------------- | ---------------- |
| Objek                     | Daun cabai       |
| Klasifikasi               | Cabai Antraknosa |
| Confidence                | 94%              |
| Termasuk 6 kelas          | Ya               |
| Visualisasi preprocessing | Tersedia         |
| Penafian indikasi awal    | Tersedia         |
| Latensi                   | 4,2 detik        |
| Status AC                 | **PASS**         |

---

## Skenario 2A — Fallback: Confidence Rendah

### AC-02 — Hasil dengan confidence rendah

**Given**

* Pengguna telah memberikan citra yang dapat diproses.
* Sistem menghasilkan salah satu dari 6 kelas target.
* **[ASUMSI-AC-01]** Confidence rendah didefinisikan sebagai **<80%**.

**When**

* Sistem selesai melakukan klasifikasi dan confidence yang dihasilkan **<80%**.

**Then**

* Sistem tetap menampilkan hasil klasifikasi dan nilai confidence.
* Sistem memberikan **peringatan bahwa confidence rendah**.
* Sistem tidak menyajikan hasil sebagai diagnosis definitif.
* Sistem menampilkan penafian bahwa hasil merupakan **indikasi awal**.
* Sistem tidak mengubah hasil menjadi kategori penyakit di luar enam kelas target.

**Contoh:**

> Hasil: **Tomat Late Blight**
> Confidence: **67%**
> ⚠️ **Confidence rendah. Hasil perlu diperiksa kembali.**
> *Hasil AI merupakan indikasi awal, bukan diagnosis definitif.*

**Status AC:** **PASS** apabila seluruh informasi tersebut tersedia.

---

## Skenario 2B — Fallback: Indikasi OOD

### AC-03 — Citra terindikasi Out-of-Distribution

**Given**

* Pengguna memberikan citra untuk dianalisis.
* Citra berpotensi merupakan objek yang berada di luar enam kategori yang dikenali.
* Sistem memiliki mekanisme indikasi OOD sesuai BR-02.
* **[ASUMSI-AC-03]** Kriteria teknis OOD ditentukan dan divalidasi sebelum implementasi final.

**When**

* Sistem mendeteksi bahwa citra berpotensi merupakan OOD.

**Then**

* Sistem memberikan indikasi bahwa citra **berpotensi berada di luar kategori yang dikenali**.
* Sistem tidak menyatakan hasil tersebut sebagai klasifikasi target yang dapat dipercaya.
* Sistem menampilkan penafian bahwa hasil AI merupakan **indikasi awal**.
* Sistem tidak memberikan diagnosis definitif.

**Contoh:**

> ⚠️ **Citra berpotensi berada di luar kategori yang dikenali sistem.**
> Hasil klasifikasi tidak dapat dianggap sebagai hasil yang dapat dipercaya.
> *AgriScan AI hanya memberikan indikasi awal dan bukan diagnosis definitif.*

**Status AC:** **PASS** apabila sistem memberikan indikasi OOD dan tidak mengklaim diagnosis.

---

## Skenario 2C — Fallback: Format Citra Tidak Valid

### AC-04 — Sistem menolak citra yang tidak dapat diproses

**Given**

* Pengguna mencoba memberikan file yang tidak dapat diproses sebagai citra.
* **[ASUMSI-AC-04]** Format citra yang diterima harus ditentukan sebelum implementasi final karena SRS belum menetapkan daftar format yang didukung.

**When**

* Pengguna mengirimkan file dengan format yang tidak didukung atau tidak dapat diproses.

**Then**

* Sistem tidak menjalankan klasifikasi AI terhadap file tersebut.
* Sistem memberikan informasi bahwa citra tidak dapat diproses.
* Sistem meminta pengguna memberikan citra yang sesuai.
* Sistem tidak menghasilkan klasifikasi palsu atau confidence level dari file yang tidak valid.

**Status AC:** **PASS** apabila file tidak valid tidak diproses sebagai hasil klasifikasi.

---

# 3. Acceptance Criteria Tambahan untuk Kualitas Fitur

### AC-05 — Cakupan Enam Kelas

**Given**

* Model telah digunakan untuk melakukan klasifikasi.

**When**

* Sistem menghasilkan prediksi.

**Then**

* Hasil normal sistem harus berasal dari tepat **6 kelas target**:

  * Cabai Normal
  * Cabai Antraknosa
  * Cabai Leaf Curl
  * Tomat Normal
  * Tomat Early Blight
  * Tomat Late Blight

**Target:** **6/6 kelas terintegrasi**.

---

### AC-06 — Confidence Selalu Ditampilkan

**Given**

* Sistem berhasil menghasilkan prediksi.

**When**

* Hasil prediksi ditampilkan.

**Then**

* Confidence level harus tersedia pada **100% hasil prediksi**.

**Target:** **100%**.

---

### AC-07 — Batas Klaim AI

**Given**

* Sistem menampilkan hasil klasifikasi.

**When**

* Pengguna melihat hasil deteksi.

**Then**

* Sistem harus menyatakan bahwa hasil merupakan **indikasi awal**.
* Sistem tidak boleh menyatakan bahwa hasil tersebut merupakan diagnosis definitif.
* Sistem tidak boleh memosisikan AI sebagai pengganti pakar.

**Target:** **100% hasil deteksi memiliki penafian/batas klaim AI.**

---

# 4. Ringkasan Acceptance Criteria

| ID        | Skenario           | Kondisi Utama                      | Target                                           | Traceability                                    |
| --------- | ------------------ | ---------------------------------- | ------------------------------------------------ | ----------------------------------------------- |
| **AC-01** | Sukses             | Confidence tinggi                  | ≥80% **[ASUMSI]**, latensi ≤5 detik **[ASUMSI]** | US-01, US-05, US-06, US-09, US-13, US-14, US-15 |
| **AC-02** | Confidence rendah  | Confidence <80% **[ASUMSI]**       | Peringatan ditampilkan                           | US-09 + BR-01                                   |
| **AC-03** | OOD                | Citra terindikasi di luar kategori | Indikasi OOD ditampilkan                         | BR-02, US-11                                    |
| **AC-04** | Format tidak valid | File tidak dapat diproses          | Tidak dilakukan klasifikasi                      | FR-01                                           |
| **AC-05** | Cakupan kelas      | Klasifikasi normal                 | 6/6 kelas                                        | FR-03, NFR-03, BR-04                            |
| **AC-06** | Confidence         | Prediksi berhasil                  | 100% hasil memiliki confidence                   | FR-04, NFR-09, BR-01                            |
| **AC-07** | Transparansi       | Hasil ditampilkan                  | 100% memiliki penafian indikasi awal             | FR-10, NFR-11, NFR-15, BR-03                    |

### Catatan penting untuk finalisasi QA

Ada **dua parameter yang belum ditetapkan oleh SRS**, sehingga angka di atas tidak boleh dianggap sebagai fakta dari riset:

* **Ambang confidence ≥80%** → **[ASUMSI-AC-01]**
* **Latensi AI ≤5 detik** → **[ASUMSI-AC-02]**

Keduanya perlu **ditentukan dan divalidasi oleh Product Owner/Tim Developer** sebelum Acceptance Criteria dijadikan kriteria penerimaan final. Demikian pula, ambang OOD dan format citra yang didukung perlu ditetapkan sebelum pengujian implementasi.
