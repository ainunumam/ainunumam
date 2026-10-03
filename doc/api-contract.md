# API Contract — AgriScan AI

## 1. Tujuan

Dokumen ini menjelaskan keputusan desain API AgriScan AI berdasarkan LLD/HLD,
User Stories, dan OpenAPI 3.0.

## 2. Endpoint

| Method | Path | Tag | Fungsi |
|---|---|---|---|
| POST | `/api/v1/detect` | AI | Menganalisis citra tanaman cabai/tomat |

Tidak ditambahkan endpoint lain karena LLD hanya mendefinisikan endpoint tersebut.

## 3. Request

Content-Type:

`multipart/form-data`

Field wajib:

- `image`
- Format: JPG/JPEG/PNG
- Maksimal: 5 MB

## 4. Response AI

Response `200` mendukung tiga skenario:

1. `HIGH_CONFIDENCE`: confidence >= 70%.
2. `LOW_CONFIDENCE`: 50% <= confidence < 70%.
3. `POTENTIAL_OOD`: confidence < 50% atau terindikasi OOD.

Data response terdiri dari:

- `prediction`
- `preprocessing`
- `warning` (opsional/null)
- `disclaimer`

## 5. Kelas Model

Enam kelas:

- Cabai Normal
- Cabai Antraknosa
- Cabai Leaf Curl
- Tomat Normal
- Tomat Early Blight
- Tomat Late Blight

## 6. Error

| HTTP | Code |
|---|---|
| 400 | INVALID_IMAGE_FORMAT |
| 400 | IMAGE_TOO_LARGE |
| 400 | INVALID_IMAGE_DATA |
| 408 | MODEL_TIMEOUT |
| 422 | INVALID_REQUEST |
| 429 | RATE_LIMIT_EXCEEDED |
| 500 | PREPROCESSING_FAILED |
| 503 | MODEL_UNAVAILABLE |
| 503 | MODEL_INFERENCE_FAILED |

## 7. Database

- `prediction_log`: metadata hasil deteksi.
- `evaluation_run`: sesi evaluasi model.
- `real_world_test`: sampel pengujian lapangan.
- `class_metric`: metrik per kelas.

`Prediction`, `Warning`, `DetectionResponse`, dan `ErrorResponse` merupakan
schema API/Pydantic, bukan tabel database.

## 8. Keputusan teknis

- Backend: FastAPI.
- Schema: Pydantic v2.
- ORM: SQLAlchemy 2.0.
- Database: SQLite untuk development/prototype dan PostgreSQL untuk staging/production.
- AI inference: CNN + ONNX Runtime server-side.
- UUID digunakan untuk primary key.
- Waktu menggunakan datetime timezone-aware dan UTC pada aplikasi.

## 9. Asumsi

- [ASUMSI-01] URL production masih placeholder.
- [ASUMSI-02] Authentication bearer belum diwajibkan karena belum ada requirement pada LLD.
- [ASUMSI-03] `image_reference` bersifat path/URL sementara; kebijakan retensi belum ditentukan.
- [ASUMSI-04] Format `model_version` belum ditentukan lebih lanjut.
