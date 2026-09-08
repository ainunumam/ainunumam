# DRAF Software Requirements Specification (SRS)

## AgriScan AI — Sistem Deteksi Dini Penyakit Tanaman Cabai dan Tomat

> **Status:** Draf SRS ringkas
> **Platform:** Website One-Page App
> **Acuan kualitas:** ISO/IEC 25010 — Functional Suitability, Performance Efficiency, Usability, Reliability, Security/Privacy
> **Prioritas:** MoSCoW

---

# 1. Tujuan, Scope, dan Definisi Istilah

## 1.1 Tujuan

SRS ini mendefinisikan kebutuhan perangkat lunak untuk **AgriScan AI**, yaitu aplikasi web yang membantu pengguna memperoleh indikasi awal kondisi tanaman cabai dan tomat melalui analisis citra menggunakan model AI berbasis CNN.

Dokumen ini menjadi acuan implementasi fitur dan evaluasi kualitas prototype selama periode pengembangan maksimal tiga bulan.

## 1.2 Scope

### Dalam scope

AgriScan AI mencakup:

* Pengambilan atau pengunggahan citra tanaman.
* Analisis citra menggunakan AI.
* Klasifikasi enam kelas:

  1. Cabai Normal
  2. Cabai Antraknosa
  3. Cabai Leaf Curl
  4. Tomat Normal
  5. Tomat Early Blight
  6. Tomat Late Blight
* Perhitungan dan tampilan confidence level.
* Visualisasi prapemrosesan citra.
* Peringatan hasil dengan confidence rendah.
* Indikasi penanganan objek yang berpotensi OOD.
* Panduan pengambilan gambar.
* Evaluasi performa berdasarkan dataset uji dan citra nyata.

### Di luar scope

* Diagnosis definitif.
* Rekomendasi pengobatan atau dosis pestisida.
* Prediksi hasil panen.
* Deteksi seluruh penyakit tanaman.
* Dukungan tanaman selain cabai dan tomat.
* Pemantauan seluruh kondisi perkebunan secara menyeluruh.

## 1.3 Definisi Istilah

| Istilah              | Definisi                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------ |
| **AI**               | Kecerdasan buatan yang digunakan untuk menganalisis citra tanaman.                         |
| **CNN**              | Convolutional Neural Network yang digunakan untuk klasifikasi citra.                       |
| **Confidence Level** | Nilai yang menunjukkan tingkat keyakinan model terhadap hasil klasifikasi.                 |
| **OOD**              | *Out-of-Distribution*, yaitu objek/citra yang berada di luar kategori yang dikenali model. |
| **Preprocessing**    | Tahap pengolahan awal citra sebelum dianalisis oleh model.                                 |
| **Dataset Uji**      | Data yang digunakan untuk mengevaluasi performa model sebagaimana tercantum dalam riset.   |
| **Real-World Test**  | Pengujian menggunakan citra nyata melalui aplikasi web.                                    |
| **Precision**        | Metrik untuk mengukur ketepatan prediksi positif suatu kelas.                              |
| **Recall**           | Metrik untuk mengukur kemampuan model menemukan sampel suatu kelas.                        |
| **F1-Score**         | Metrik gabungan antara precision dan recall.                                               |

---

# 2. User & Stakeholder, Lingkungan Operasi, Asumsi & Dependensi

## 2.1 User dan Stakeholder

| Aktor                                  | Peran dalam Sistem | Kebutuhan Utama                                |
| -------------------------------------- | ------------------ | ---------------------------------------------- |
| Petani cabai dan tomat                 | Pengguna utama     | Memperoleh indikasi awal penyakit secara cepat |
| Penyuluh pertanian lapangan            | Pengguna pendukung | Membantu pemeriksaan tanaman di lapangan       |
| Pengelola perkebunan hortikultura      | Pengguna pendukung | Mendukung pemantauan kondisi tanaman           |
| Tim Developer Web/AI                   | Pengembang         | Mengembangkan dan memperbaiki sistem/model     |
| Peneliti/Pakar Hama & Penyakit Tanaman | Validator          | Memvalidasi kategori dan hasil                 |
| Pengelola Platform/Mitra Pertanian     | Pengelola          | Mendukung keberlanjutan platform               |

## 2.2 Lingkungan Operasi

* Sistem beroperasi sebagai **Website One-Page App**.
* Perangkat pengguna diasumsikan berupa **smartphone Android dengan kamera yang memadai**.
* Sistem digunakan pada kondisi lapangan yang memiliki variasi pencahayaan, sudut pengambilan gambar, dan kualitas kamera.
* Pengguna dapat memiliki **koneksi internet terbatas**.

## 2.3 Asumsi

| ID    | Asumsi                                                                                         |
| ----- | ---------------------------------------------------------------------------------------------- |
| AS-01 | Pengguna memiliki smartphone Android dengan kamera yang memadai.                               |
| AS-02 | Pengguna dapat mengakses web app meskipun koneksi internet terbatas.                           |
| AS-03 | Pengguna memahami bahwa hasil AI merupakan indikasi awal, bukan diagnosis definitif.           |
| AS-04 | Dataset pelatihan prototype belum mencakup seluruh variasi kondisi lapangan.                   |
| AS-05 | Prototype dapat diselesaikan dalam waktu maksimal tiga bulan dengan sumber daya yang tersedia. |

## 2.4 Dependensi

* Dataset berjumlah **3.734 citra** dari PlantVillage dan dataset mandiri.
* Model CNN yang digunakan untuk enam kelas target.
* Data pengujian dataset dan real-world test sebagaimana tersedia pada riset.
* Validasi kategori dan hasil oleh **Peneliti/Pakar Hama & Penyakit Tanaman**.

---

# 3. Functional Requirements (FR)

| ID FR     | Deskripsi Kebutuhan (Pola)                                                                                                                                                                                 | Prioritas MoSCoW | Metode Verifikasi |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------- |
| **FR-01** | Sistem harus dapat **menerima citra tanaman cabai atau tomat** saat pengguna melakukan pengambilan atau pengunggahan citra → **citra tersedia untuk dianalisis**                                           | Must Have        | Uji               |
| **FR-02** | Sistem harus dapat **melakukan analisis citra menggunakan model CNN** saat citra yang valid tersedia → **hasil klasifikasi tanaman**                                                                       | Must Have        | Demonstrasi       |
| **FR-03** | Sistem harus dapat **mengklasifikasikan citra ke dalam enam kategori target** saat proses analisis selesai → **satu hasil kategori dari enam kelas target**                                                | Must Have        | Uji               |
| **FR-04** | Sistem harus dapat **menghasilkan confidence level** saat model menghasilkan klasifikasi → **nilai confidence pada hasil prediksi**                                                                        | Must Have        | Uji               |
| **FR-05** | Sistem harus dapat **menampilkan hasil klasifikasi dan confidence level** saat analisis citra selesai → **informasi hasil deteksi kepada pengguna**                                                        | Must Have        | Demonstrasi       |
| **FR-06** | Sistem harus dapat **menampilkan visualisasi prapemrosesan citra** saat citra telah melalui tahap prapemrosesan → **visualisasi citra hasil prapemrosesan**                                                | Must Have        | Demonstrasi       |
| **FR-07** | Sistem harus dapat **memberikan peringatan terhadap hasil dengan confidence rendah** saat confidence berada pada kategori rendah → **peringatan kepada pengguna untuk berhati-hati terhadap hasil**        | Should Have      | Uji               |
| **FR-08** | Sistem harus dapat **memberikan indikasi bahwa citra berpotensi berada di luar kategori yang dikenali** saat citra terindikasi OOD → **indikasi OOD dan hasil yang tidak diklaim sebagai diagnosis pasti** | Should Have      | Uji               |
| **FR-09** | Sistem harus dapat **menampilkan panduan pengambilan gambar** saat pengguna akan memberikan citra untuk dianalisis → **panduan pengambilan citra**                                                         | Should Have      | Demonstrasi       |
| **FR-10** | Sistem harus dapat **menampilkan informasi bahwa hasil AI merupakan indikasi awal** saat hasil klasifikasi diberikan → **batasan penggunaan hasil AI**                                                     | Must Have        | Inspeksi          |
| **FR-11** | Sistem harus dapat **mendukung evaluasi terhadap enam kelas target** saat proses evaluasi model dilakukan → **nilai Precision, Recall, dan F1-Score untuk setiap kelas**                                   | Must Have        | Uji               |
| **FR-12** | Sistem harus dapat **mendukung pengujian menggunakan citra nyata** saat evaluasi real-world dilakukan → **hasil evaluasi performa pada citra nyata**                                                       | Must Have        | Uji               |

### Catatan batas FR

FR di atas **tidak mendefinisikan arsitektur, endpoint, struktur database, algoritma preprocessing, atau rancangan UI**, karena detail tersebut berada pada dokumen desain/arsitektur teknis dan bukan ruang lingkup SRS ini.

---

# 4. Non-Functional Requirements (NFR)

| ID NFR     | Kategori ISO/IEC 25010 | Metrik & Target                                                                                                                                           | Kondisi Pengukuran                                                                                           |
| ---------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **NFR-01** | Functional Suitability | Akurasi dataset uji **≥91%**                                                                                                                              | Dihitung dari prediksi benar ÷ seluruh sampel dataset uji × 100%                                             |
| **NFR-02** | Functional Suitability | Akurasi real-world **≥75%**                                                                                                                               | Dihitung pada pengujian nyata menggunakan **60 sampel**                                                      |
| **NFR-03** | Functional Suitability | Cakupan klasifikasi **6/6 kelas**                                                                                                                         | Seluruh enam kategori target tersedia dan dapat dievaluasi                                                   |
| **NFR-04** | Functional Suitability | Precision, Recall, F1-Score tersedia untuk **6/6 kelas**                                                                                                  | Evaluasi dilakukan terhadap setiap kelas                                                                     |
| **NFR-05** | Functional Suitability | Recall Tomat Late Blight dipantau terhadap baseline **0,7594**                                                                                            | Evaluasi per kelas                                                                                           |
| **NFR-06** | Functional Suitability | Precision dan Recall Cabai Leaf Curl dipantau terhadap baseline **0,9711 dan 0,9619**                                                                     | Evaluasi per kelas                                                                                           |
| **NFR-07** | Performance Efficiency | **[ASUMSI-NFR-01]** Latensi AI harus cukup rendah sehingga hasil dapat digunakan untuk pemeriksaan lapangan tanpa waktu tunggu yang menghambat penggunaan | Diukur dari saat citra siap dianalisis hingga hasil klasifikasi tersedia pada lingkungan pengujian prototype |
| **NFR-08** | Performance Efficiency | Pemrosesan citra tetap **ringan sesuai batasan prototype**                                                                                                | Pengujian menggunakan lingkungan prototype dengan keterbatasan infrastruktur AI                              |
| **NFR-09** | Usability              | Confidence level tersedia pada **100% hasil prediksi**                                                                                                    | Pengujian seluruh hasil prediksi                                                                             |
| **NFR-10** | Usability              | Panduan pengambilan citra tersedia bagi pengguna                                                                                                          | Inspeksi dan demonstrasi penggunaan                                                                          |
| **NFR-11** | Usability              | Hasil klasifikasi dan confidence level dapat dipahami sebagai informasi indikasi awal                                                                     | Inspeksi terhadap penyajian informasi dan pengujian penggunaan                                               |
| **NFR-12** | Reliability            | Sistem mampu mempertahankan evaluasi terhadap variasi kondisi nyata yang menjadi sumber penurunan akurasi                                                 | Pengujian dengan citra nyata yang memiliki variasi pencahayaan, sudut, dan kualitas kamera                   |
| **NFR-13** | Security               | **[ASUMSI-NFR-02]** Sistem tidak boleh mengungkapkan data pengguna yang tidak diperlukan untuk fungsi deteksi                                             | Inspeksi perilaku sistem selama penggunaan prototype                                                         |
| **NFR-14** | Privacy                | **[ASUMSI-NFR-03]** Citra pengguna hanya digunakan sesuai kebutuhan fungsi analisis dan tidak diklaim sebagai data untuk tujuan lain                      | Inspeksi terhadap perilaku dan informasi penggunaan sistem                                                   |
| **NFR-15** | Reliability            | Sistem harus memberikan hasil yang dapat dibedakan dari klaim diagnosis definitif                                                                         | Inspeksi terhadap hasil dan informasi batasan AI                                                             |

> **Catatan penting:** PRD tidak memberikan angka target latensi, spesifikasi perangkat minimum, ukuran file citra, atau SLA. Karena itu, SRS tidak menetapkan angka baru untuk parameter tersebut. Target **[ASUMSI-NFR-01]** perlu divalidasi sebelum menjadi requirement final.

---

# 5. Kebutuhan Data Minimum Fitur AI

Alur kebutuhan data pada level fungsional:

**Input Citra → Preprocessing → Model CNN → Output Klasifikasi + Confidence**

## 5.1 Input Citra

| Elemen          | Kebutuhan                                                                               |
| --------------- | --------------------------------------------------------------------------------------- |
| Objek           | Daun/buah tanaman cabai atau tomat                                                      |
| Sumber          | Pengambilan atau pengunggahan citra oleh pengguna                                       |
| Kategori target | 6 kelas                                                                                 |
| Kondisi data    | Dapat berasal dari kondisi nyata dengan variasi pencahayaan, sudut, dan kualitas kamera |

## 5.2 Preprocessing

Sistem harus melakukan **prapemrosesan terhadap citra sebelum klasifikasi** dan menyediakan visualisasi hasil prapemrosesan kepada pengguna.

Detail teknik preprocessing **tidak ditentukan dalam SRS** karena tidak tersedia dalam PRD.

## 5.3 Model dan Output

Model AI berbasis **CNN** harus menghasilkan:

1. Kategori hasil klasifikasi.
2. Confidence level.
3. Informasi yang memungkinkan hasil berconfidence rendah diberikan peringatan.
4. Indikasi OOD apabila mekanisme OOD telah tersedia dalam scope implementasi.

### Enam kelas output

```text
Cabai Normal
Cabai Antraknosa
Cabai Leaf Curl
Tomat Normal
Tomat Early Blight
Tomat Late Blight
```

---

# 6. Aturan Bisnis Hasil Riset

## BR-01 — Confidence Level

Setiap hasil klasifikasi **harus disertai confidence level**.

**Dasar:** PRD menetapkan confidence level tersedia pada 100% hasil prediksi.

### Ambang confidence

PRD hanya menyatakan adanya kebutuhan **peringatan hasil berkepercayaan rendah**, tetapi **tidak memberikan angka ambang confidence**.

Karena itu:

> **[ASUMSI-BR-01]** Nilai ambang confidence rendah harus ditentukan melalui evaluasi/validasi sebelum implementasi final dan tidak boleh ditetapkan secara arbitrer hanya dari SRS ini.

---

## BR-02 — Penanganan OOD

Jika citra terindikasi berada di luar enam kategori target, sistem harus memberikan **indikasi bahwa hasil tidak dapat dipercaya sebagai klasifikasi kategori target**.

Tujuannya adalah mengurangi risiko sistem memaksakan objek yang tidak dikenali menjadi salah satu dari enam kelas.

**Dasar:** pada pengujian nyata, ketiadaan mekanisme OOD disebut sebagai salah satu penyebab penurunan akurasi.

Namun:

> **[ASUMSI-BR-02]** Kriteria teknis untuk menentukan OOD belum ditentukan dalam PRD dan harus divalidasi sebelum implementasi.

---

## BR-03 — Batas Klaim AI

Hasil AgriScan AI hanya boleh diposisikan sebagai **indikasi awal**.

Sistem tidak boleh mengklaim:

* diagnosis definitif;
* pengganti pakar;
* kepastian bahwa tanaman benar-benar terserang penyakit berdasarkan hasil AI saja.

**Dasar:** ASUMSI-03 dan non-goals PRD.

---

## BR-04 — Enam Kelas Target

Klasifikasi normal pada prototype dibatasi pada enam kategori yang telah ditentukan.

Sistem tidak dituntut untuk memberikan klasifikasi penyakit di luar keenam kategori tersebut.

---

## BR-05 — Evaluasi Kelas Prioritas

Evaluasi harus memberikan perhatian khusus terhadap:

* **Cabai Leaf Curl**, karena kesalahan pada pengujian nyata mencapai 50%.
* **Tomat Normal**, karena kesalahan pada pengujian nyata mencapai 40%.
* **Tomat Early Blight vs Tomat Late Blight**, karena terdapat 14 sampel salah pada dataset uji.
* **Tomat Late Blight**, karena memiliki Recall terendah sebesar 0,7594.

---

# 7. Matriks Traceability

| Requirement | Fitur PRD                         | Bukti/Dasar Riset                                                               |
| ----------- | --------------------------------- | ------------------------------------------------------------------------------- |
| **FR-01**   | Pengambilan/upload citra          | Fitur Must Have: pengambilan/upload citra                                       |
| **FR-02**   | ★ Deteksi penyakit berbasis citra | AI inti: CNN untuk klasifikasi visual                                           |
| **FR-03**   | ★ Klasifikasi 6 kelas             | Riset: 6 kelas target                                                           |
| **FR-04**   | ★ Confidence level                | PRD: confidence level pada hasil prediksi                                       |
| **FR-05**   | Tampilan hasil deteksi            | Fitur Must Have: tampilan hasil deteksi                                         |
| **FR-06**   | ★ Visualisasi prapemrosesan       | Fitur Must Have: visualisasi prapemrosesan                                      |
| **FR-07**   | ★ Peringatan confidence rendah    | Fitur Should Have                                                               |
| **FR-08**   | ★ Penanganan OOD                  | Fitur Should Have; OOD menjadi penyebab penurunan akurasi                       |
| **FR-09**   | Panduan pengambilan gambar        | Fitur Should Have; mitigasi variasi pencahayaan/sudut/kualitas                  |
| **FR-10**   | Batas klaim AI                    | PRD: AI sebagai indikasi awal, bukan diagnosis definitif                        |
| **FR-11**   | Evaluasi per kelas                | KPI: 6/6 kelas dievaluasi Precision, Recall, F1                                 |
| **FR-12**   | Real-world testing                | Bukti riset: pengujian web menggunakan 60 sampel                                |
| **NFR-01**  | Akurasi dataset                   | Riset: akurasi dataset uji 91%                                                  |
| **NFR-02**  | Akurasi real-world                | Riset: akurasi nyata 75% dari 60 sampel                                         |
| **NFR-03**  | Cakupan kelas                     | Riset: 6 kelas target                                                           |
| **NFR-04**  | Evaluasi metrik                   | KPI: Precision, Recall, F1 untuk 6/6 kelas                                      |
| **NFR-05**  | Evaluasi Late Blight              | Recall Late Blight 0,7594; F1 0,8510                                            |
| **NFR-06**  | Evaluasi Leaf Curl                | Precision 0,9711; Recall 0,9619                                                 |
| **NFR-07**  | Latensi AI                        | PRD: kebutuhan pemrosesan citra tetap ringan; angka latensi **[ASUMSI-NFR-01]** |
| **NFR-08**  | Efisiensi pemrosesan              | Konstrain: pemrosesan citra harus tetap ringan                                  |
| **NFR-09**  | Confidence                        | KPI: confidence tersedia pada 100% hasil                                        |
| **NFR-10**  | Panduan gambar                    | Fitur Should Have                                                               |
| **NFR-11**  | Usability hasil                   | Value proposition: confidence transparan dan pemeriksaan mudah                  |
| **NFR-12**  | Reliability kondisi nyata         | Riset: performa turun akibat pencahayaan, sudut/kualitas kamera                 |
| **NFR-13**  | Security                          | **[ASUMSI-NFR-02]** karena PRD tidak menetapkan kebutuhan keamanan spesifik     |
| **NFR-14**  | Privacy                           | **[ASUMSI-NFR-03]** karena PRD tidak menetapkan kebijakan privasi spesifik      |
| **NFR-15**  | Reliability/batas klaim           | PRD: AI hanya alat bantu deteksi dini                                           |

---

## Kesimpulan SRS

Secara implementatif, **baseline kebutuhan wajib AgriScan AI** dapat diringkas menjadi:

**Input citra tanaman → preprocessing → CNN → klasifikasi 6 kelas → confidence level → hasil deteksi + visualisasi preprocessing.**

Kemudian fitur **peringatan confidence rendah, indikasi OOD, dan panduan pengambilan gambar** menjadi prioritas *Should Have* untuk mengatasi masalah utama yang ditemukan dalam riset, terutama **gap akurasi 91% pada dataset menjadi 75% pada pengujian nyata**.

SRS ini sengaja **tidak menetapkan detail arsitektur, endpoint Flask, struktur database, metode preprocessing spesifik, ukuran input model, algoritma OOD, atau desain UI**, karena detail tersebut belum tersedia dalam PRD dan akan masuk ke dokumen desain teknis berikutnya.
