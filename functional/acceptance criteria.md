# MATRIKS TRACEABILITY KOMPREHENSIF — AGRISCAN AI

Matriks berikut menghubungkan kebutuhan secara **end-to-end** dari **SRS → User Story → Use Case → Acceptance Criteria → Komponen Teknis/AI → Metode Pengujian**.

> **Catatan:** Traceability menggunakan ID AC-01 s.d. AC-22 sesuai pemetaan yang diberikan. Untuk User Story yang memiliki beberapa kondisi uji, satu ID AC mewakili rangkaian kriteria Gherkin terkait User Story tersebut. Tidak ada kebutuhan baru yang ditambahkan di luar parameter yang diberikan.

## 1. Matriks Keterlacakan Utama

| ID Kebutuhan (SRS)         | ID User Story | ID Use Case                       | ID Acceptance Criteria                                                                    | Komponen Teknis & Model AI Terlibat                                   | Rencana & Metode Uji                                                 |
| -------------------------- | ------------- | --------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **FR-01 + NFR-08**         | **US-01**     | **UC-01**                         | **AC-01** — Happy Flow, boundary **≤5 MB**, invalid **>5 MB**                             | Client Browser Validation (HTML/JS), Flask API Gateway                | Unit Test validasi + Integration Test + UAT                          |
| **FR-01 + NFR-08**         | **US-02**     | **UC-01**                         | **AC-02** — Happy Flow, boundary **5 MB**, format invalid                                 | Client Browser Validation, Flask API Gateway                          | Unit Test + Integration Test + UAT                                   |
| **FR-09 + NFR-08**         | **US-03**     | **UC-01**                         | **AC-03** — Panduan tersedia sebelum input/deteksi                                        | Client Browser                                                        | UAT + Inspection                                                     |
| **FR-09 + NFR-08**         | **US-04**     | **UC-01**                         | **AC-04** — Panduan tersedia sebelum input/deteksi                                        | Client Browser                                                        | UAT + Inspection                                                     |
| **FR-02 + NFR-07**         | **US-05**     | **UC-01**                         | **AC-05** — Happy Flow, latensi **≤3,0 detik**, timeout **>3,0 detik**                    | Flask API Gateway, Image Preprocessing Engine, CNN Inference Engine   | Integration Test + End-to-End Test + Performance Test                |
| **FR-03 + NFR-03 + BR-04** | **US-06**     | **UC-01**                         | **AC-06** — Klasifikasi tepat **1 dari 6 kelas**, boundary confidence **70%**, timeout    | CNN Inference Engine, Flask API Gateway                               | Unit Test + Integration Test + Boundary Value Analysis               |
| **FR-02 + NFR-07**         | **US-07**     | **UC-01**                         | **AC-07** — Analisis AI, latensi **≤3,0 detik**, timeout **>3,0 detik**                   | Flask API Gateway, Preprocessing Engine, CNN Inference Engine         | Integration Test + Performance Test + UAT                            |
| **FR-02 + FR-03 + NFR-03** | **US-08**     | **UC-01**                         | **AC-08** — Analisis citra, input **≤5 MB**, klasifikasi 6 kelas, timeout                 | Flask API Gateway, Preprocessing Engine, CNN Inference Engine         | Integration Test + UAT + Performance Test                            |
| **FR-04 + NFR-09 + BR-01** | **US-09**     | **UC-01**                         | **AC-09** — Confidence **85%**, boundary **70%/69,99%**, timeout                          | CNN Inference Engine, Flask API Gateway                               | Unit Test + Integration Test + Boundary Value Analysis               |
| **FR-07 + BR-01**          | **US-10**     | **UC-01**                         | **AC-10** — Confidence **65%**, boundary **70%**, timeout                                 | CNN Inference Engine, Flask API Gateway                               | Unit Test + Boundary Value Analysis + Integration Test               |
| **FR-08 + BR-02**          | **US-11**     | **UC-01**                         | **AC-11** — OOD confidence **45%**, boundary **50%/49,99%**, timeout                      | CNN Inference Engine, OOD Detection/Decision Logic, Flask API Gateway | Unit Test + Integration Test + Boundary Value Analysis               |
| **FR-08 + BR-02**          | **US-12**     | **UC-01**                         | **AC-12** — OOD confidence **40%**, boundary **50%**, timeout                             | CNN Inference Engine, OOD Detection/Decision Logic, Flask API Gateway | Integration Test + Boundary Value Analysis + UAT                     |
| **FR-05 + FR-04 + NFR-09** | **US-13**     | **UC-01**                         | **AC-13** — Hasil klasifikasi + confidence **82%**, latensi **≤3,0 detik**, timeout       | CNN Inference Engine, Flask API Gateway, Client Browser               | Integration Test + End-to-End Test + UAT                             |
| **FR-06**                  | **US-14**     | **UC-01**                         | **AC-14** — Visualisasi preprocessing tersedia, termasuk input boundary **5 MB**, timeout | Image Preprocessing Engine, Client Browser, Flask API Gateway         | Unit Test + Integration Test + UAT                                   |
| **FR-10 + NFR-15 + BR-03** | **US-15**     | **UC-01**                         | **AC-15** — Disclaimer pada confidence **90%**, confidence **60%**, dan kondisi gagal     | Client Browser, Flask API Gateway                                     | Inspection + Integration Test + UAT                                  |
| **FR-10 + NFR-15 + BR-03** | **US-16**     | **UC-01**                         | **AC-16** — Disclaimer pada confidence **85%**, **65%**, dan OOD **45%**                  | Client Browser, Flask API Gateway, CNN/OOD Logic                      | UAT + Integration Test                                               |
| **FR-11 + NFR-03**         | **US-17**     | **UC-01 / Sub-UC Evaluasi Model** | **AC-17** — Precision, Recall, F1-Score tersedia untuk **6/6 kelas**                      | Model Evaluation Module, Scikit-Learn Evaluation Suite, CNN Model     | Automated Model Evaluation + Unit Test                               |
| **FR-11 + NFR-01**         | **US-18**     | **Sub-UC Evaluasi Dataset**       | **AC-18** — Akurasi **≥91%**, boundary **91,00%**, failure **90,99%**                     | Model Evaluation Module, Scikit-Learn Evaluation Suite, CNN Model     | Automated Model Evaluation + Boundary Value Analysis                 |
| **FR-12 + NFR-02**         | **US-19**     | **Sub-UC Real-World Evaluation**  | **AC-19** — Minimal **60 sampel**, target **≥75%**, contoh boundary **45/60 = 75%**       | CNN Inference Engine, Flask API Gateway, Model Evaluation Module      | End-to-End Test + Real-World Evaluation                              |
| **FR-11 + BR-05**          | **US-20**     | **Sub-UC Evaluasi Model**         | **AC-20** — Recall Late Blight baseline **0,7594**, F1 **0,8510**                         | Model Evaluation Module, Scikit-Learn Evaluation Suite, CNN Model     | Automated Model Evaluation + Regression Test                         |
| **FR-11 + BR-05**          | **US-21**     | **Sub-UC Evaluasi Model**         | **AC-21** — Precision **0,9711**, Recall **0,9619**, error lapangan baseline **50%**      | Model Evaluation Module, Scikit-Learn Evaluation Suite, CNN Model     | Automated Model Evaluation + Real-World Evaluation + Regression Test |
| **FR-11 + BR-05**          | **US-22**     | **Sub-UC Evaluasi Model**         | **AC-22** — Cross-misclassification Early/Late Blight baseline **14 sampel**              | Model Evaluation Module, Scikit-Learn Evaluation Suite, CNN Model     | Confusion Matrix Analysis + Regression Test                          |

---

# 2. Traceability NFR & Business Rules

Bagian ini memperjelas bagaimana kebutuhan kualitas dan aturan bisnis diturunkan ke User Story dan Acceptance Criteria. Dengan demikian, **NFR/BR tidak berdiri sendiri**, tetapi dapat ditelusuri sampai ke pengujian.

| NFR / BR                                            | FR Pendukung | User Story          | UC                           | AC                      | Bukti Pengujian                                                               |
| --------------------------------------------------- | ------------ | ------------------- | ---------------------------- | ----------------------- | ----------------------------------------------------------------------------- |
| **NFR-01 — Akurasi dataset ≥91%**                   | FR-11        | US-18               | Sub-UC Evaluasi Dataset      | **AC-18**               | Akurasi model ≥91%; boundary 91,00% diterima dan 90,99% ditolak               |
| **NFR-02 — Akurasi real-world ≥75% dari 60 sampel** | FR-12        | US-19               | Sub-UC Real-World Evaluation | **AC-19**               | Minimal 60 sampel; 45/60 = 75% memenuhi baseline                              |
| **NFR-07 — Latensi ≤3,0 detik**                     | FR-02        | US-05, US-07, US-08 | UC-01                        | **AC-05, AC-07, AC-08** | Performance/Integration Test; kondisi >3,0 detik diperlakukan sebagai timeout |
| **NFR-08 — JPG/JPEG/PNG ≤5 MB**                     | FR-01        | US-01, US-02        | UC-01                        | **AC-01, AC-02**        | Boundary Value Analysis: 5 MB diterima; >5 MB ditolak                         |
| **NFR-09 — Confidence tampil 100%**                 | FR-04        | US-09, US-13        | UC-01                        | **AC-09, AC-13**        | Integration Test terhadap seluruh hasil prediksi                              |
| **BR-01 — Confidence ≥70%**                         | FR-04        | US-09, US-13        | UC-01                        | **AC-09, AC-13**        | Boundary: 70% dikategorikan confidence tinggi                                 |
| **BR-01/BR-03 — Confidence <70%**                   | FR-07        | US-10               | UC-01                        | **AC-10**               | Boundary: 69,99% menghasilkan peringatan                                      |
| **BR-02 — OOD jika <50%**                           | FR-08        | US-11, US-12        | UC-01                        | **AC-11, AC-12**        | Boundary: 49,99% → OOD; 50% → bukan OOD berdasarkan threshold confidence      |
| **BR-02 — OOD jika di luar 6 kelas**                | FR-08        | US-11, US-12        | UC-01                        | **AC-11, AC-12**        | Integration Test terhadap kondisi objek di luar target                        |
| **BR-03/NFR-15 — Disclaimer 100%**                  | FR-10        | US-15, US-16        | UC-01                        | **AC-15, AC-16**        | Inspection + UAT pada confidence tinggi/rendah/OOD                            |
| **BR-04 — Tepat 6 kelas target**                    | FR-03        | US-06               | UC-01                        | **AC-06**               | Integration Test dan validasi output                                          |
| **BR-05 — Late Blight**                             | FR-11        | US-20               | Sub-UC Evaluasi Model        | **AC-20**               | Recall 0,7594; F1 0,8510                                                      |
| **BR-05 — Leaf Curl**                               | FR-11        | US-21               | Sub-UC Evaluasi Model        | **AC-21**               | Precision 0,9711; Recall 0,9619; error lapangan 50%                           |
| **BR-05 — Tomat Normal**                            | FR-11        | US-21/US-22         | Sub-UC Evaluasi Model        | **AC-21/AC-22**         | Kesalahan real-world dipantau terhadap baseline 40%                           |
| **BR-05 — Early vs Late Blight**                    | FR-11        | US-22               | Sub-UC Evaluasi Model        | **AC-22**               | Cross-misclassification dibandingkan dengan baseline 14 sampel                |

---

# 3. Traceability End-to-End per Epik

## Epik 1 — Penginputan & Panduan Citra

```text
FR-01
  ↓
US-01 / US-02
  ↓
UC-01
  ↓
AC-01 / AC-02
  ↓
Client Browser Validation + Flask API
  ↓
Unit Test + Integration Test + UAT
```

```text
FR-09
  ↓
US-03 / US-04
  ↓
UC-01
  ↓
AC-03 / AC-04
  ↓
Client Browser
  ↓
UAT + Inspection
```

### Coverage Epik 1: **Lengkap**

Semua US-01 s.d. US-04 memiliki FR, UC, AC, komponen, dan metode pengujian.

---

## Epik 2 — Analisis & Klasifikasi AI

```text
FR-02
  ↓
US-05 / US-07 / US-08
  ↓
UC-01
  ↓
AC-05 / AC-07 / AC-08
  ↓
Preprocessing → CNN Inference → Flask
  ↓
Integration + Performance + UAT
```

```text
FR-03 + BR-04
  ↓
US-06
  ↓
UC-01
  ↓
AC-06
  ↓
CNN 6-Class Model
  ↓
Integration + Boundary Test
```

```text
FR-04 + NFR-09 + BR-01
  ↓
US-09
  ↓
UC-01
  ↓
AC-09
  ↓
CNN Inference + Flask
  ↓
Unit + Integration + Boundary Test
```

```text
FR-07 + BR-01
  ↓
US-10
  ↓
UC-01
  ↓
AC-10
  ↓
Confidence Decision Logic
  ↓
Boundary + Integration Test
```

```text
FR-08 + BR-02
  ↓
US-11 / US-12
  ↓
UC-01
  ↓
AC-11 / AC-12
  ↓
CNN + OOD Decision Logic
  ↓
Integration + Boundary Test
```

### Coverage Epik 2: **Lengkap**

Semua US-05 s.d. US-12 memiliki keterlacakan ke FR dan AC.

---

# Epik 3 — Penyajian Hasil & Transparansi

```text
FR-05 + FR-04
  ↓
US-13
  ↓
UC-01
  ↓
AC-13
  ↓
CNN + Flask + Client Browser
  ↓
Integration + E2E + UAT
```

```text
FR-06
  ↓
US-14
  ↓
UC-01
  ↓
AC-14
  ↓
Image Preprocessing Engine
  ↓
Integration + UAT
```

```text
FR-10 + NFR-15 + BR-03
  ↓
US-15 / US-16
  ↓
UC-01
  ↓
AC-15 / AC-16
  ↓
Client Browser + Flask
  ↓
Inspection + Integration + UAT
```

### Coverage Epik 3: **Lengkap**

Semua US-13 s.d. US-16 memiliki FR, UC, AC, komponen, dan metode pengujian.

---

# Epik 4 — Evaluasi & Performa

```text
FR-11
  ↓
US-17
  ↓
AC-17
  ↓
Model Evaluation Module
  ↓
Precision + Recall + F1
  ↓
6/6 Kelas
```

```text
FR-11 + NFR-01
  ↓
US-18
  ↓
AC-18
  ↓
Automated Model Evaluation
  ↓
Akurasi ≥91%
```

```text
FR-12 + NFR-02
  ↓
US-19
  ↓
AC-19
  ↓
Real-World Evaluation
  ↓
≥75% dari ≥60 sampel
```

```text
FR-11 + BR-05
  ↓
US-20 / US-21 / US-22
  ↓
AC-20 / AC-21 / AC-22
  ↓
Model Evaluation Module
  ↓
Regression + Confusion Matrix Analysis
```

### Coverage Epik 4: **Lengkap**

Semua US-17 s.d. US-22 memiliki keterlacakan sampai ke Acceptance Criteria dan metode pengujian.

---

# 4. Coverage Analysis

| Area                |                         Jumlah | Status       |
| ------------------- | -----------------------------: | ------------ |
| FR SRS              |                      **12/12** | ✅ Terpetakan |
| User Stories        |                      **22/22** | ✅ Terpetakan |
| Acceptance Criteria |                      **22/22** | ✅ Terpetakan |
| Use Case utama      |                      **UC-01** | ✅ Terpetakan |
| NFR utama           | **NFR-01, 02, 07, 08, 09, 15** | ✅ Terpetakan |
| Business Rules      |           **BR-01 s.d. BR-05** | ✅ Terpetakan |
| 6 kelas AI          |                        **6/6** | ✅ Terpetakan |
| Dataset accuracy    |                       **≥91%** | ✅ Teruji     |
| Real-world accuracy |          **≥75% / ≥60 sampel** | ✅ Teruji     |
| Latensi             |                 **≤3,0 detik** | ✅ Teruji     |
| File input          |        **JPG/JPEG/PNG, ≤5 MB** | ✅ Teruji     |
| Confidence tinggi   |                       **≥70%** | ✅ Teruji     |
| Confidence rendah   |                       **<70%** | ✅ Teruji     |
| OOD confidence      |                       **<50%** | ✅ Teruji     |
| Disclaimer          |                 **100% hasil** | ✅ Teruji     |

---

# 5. Status Traceability

### 🟢 Coverage Lengkap

Berdasarkan konteks yang diberikan, **tidak terdapat FR-01 s.d. FR-12 atau US-01 s.d. US-22 yang kehilangan turunan Acceptance Criteria**.

Rantai keterlacakan utama telah terbentuk:

> **SRS FR/NFR/BR → User Story → Use Case → Acceptance Criteria → Komponen Eksekusi → Metode Pengujian**

### Titik Kendali QA Paling Kritis

1. **Input:** JPG/JPEG/PNG dan **≤5 MB**.
2. **AI:** tepat **6 kelas target**.
3. **Performance:** inferensi **≤3,0 detik**.
4. **Confidence:** **≥70%** = indikasi dominan.
5. **Confidence rendah:** **<70%** = *Hasil Meragukan / Confidence Rendah*.
6. **OOD:** **<50%** atau objek bukan cabai/tomat.
7. **Disclaimer:** muncul pada **100% hasil analisis**.
8. **Dataset:** akurasi **≥91%**.
9. **Real-world:** akurasi **≥75%** dari minimal **60 sampel**.
10. **Evaluasi model:** Precision, Recall, dan F1-Score untuk **6/6 kelas**.
11. **Late Blight:** Recall **0,7594** dan F1 **0,8510** sebagai baseline pemantauan.
12. **Leaf Curl:** Precision **0,9711**, Recall **0,9619**, dengan perhatian terhadap error lapangan **50%**.
13. **Tomat Normal:** error lapangan dipantau terhadap baseline **40%**.
14. **Early Blight vs Late Blight:** cross-misclassification dipantau terhadap **14 sampel salah**.

Dengan matriks ini, setiap kebutuhan utama AgriScan AI dapat ditelusuri sampai ke **bukti pengujian konkret**, sehingga dapat digunakan sebagai dasar **QA Test Plan, Test Case, Regression Test, dan UAT** tanpa perlu menambahkan kebutuhan baru di luar SRS.
