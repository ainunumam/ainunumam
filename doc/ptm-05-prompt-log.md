# PTM-05 Prompt Log — AgriScan AI

## Sesi 1 — D.1 OpenAPI

**Target Prompt:** D.1 OpenAPI

**Peran:**
Backend architect senior, ahli REST API dan OpenAPI 3.0.

**Tujuan:**
Membuat draft OpenAPI 3.0 berdasarkan LLD dan User Stories.

**Input utama:**
- POST `/api/v1/detect`
- multipart/form-data
- field `image`
- JPG/JPEG/PNG maksimal 5 MB
- response prediction, preprocessing, warning, disclaimer
- status confidence: HIGH_CONFIDENCE, LOW_CONFIDENCE, POTENTIAL_OOD
- error codes LLD
- stack FastAPI + SQLAlchemy + ONNX Runtime

**Hasil:**
OpenAPI hanya memiliki satu endpoint, yaitu `POST /api/v1/detect`, dengan tag `AI`
dan schema reusable untuk Prediction, Preprocessing, Warning, DetectionResponse,
ErrorDetail, dan ErrorResponse.

**Revisi manual:**
- Memastikan tidak ada endpoint tambahan.
- Memastikan enam kelas target dicantumkan.
- Menandai gap sebagai `[ASUMSI-XX]`.

## Sesi 2 — D.2 ERD/Skema

**Target Prompt:** D.2 ERD/Skema

**Tujuan:**
Membuat ERD Mermaid dan schema Pydantic/SQLAlchemy yang sinkron dengan OpenAPI
dan entitas Data Store dari LLD/HLD.

**Entitas:**
- prediction_log
- evaluation_run
- real_world_test
- class_metric

**Hasil:**
- ERD dengan relasi evaluation_run 1-to-many ke real_world_test.
- ERD dengan relasi evaluation_run 1-to-many ke class_metric.
- Pydantic v2 menggunakan Enum, Field constraints, dan model_validator.
- SQLAlchemy 2.0 menggunakan UUID, datetime timezone-aware, FK, unique,
  index, dan check constraint.

**Revisi manual:**
- Menyesuaikan `class` API dengan alias Pydantic `class_`.
- Memastikan confidence berada pada 0–1.
- Menambahkan validasi minimal 60 sample untuk evaluasi real-world pada service layer.

## Sesi 3 — Iterasi Lanjutan

**Masalah/gap yang ditemukan:**
1. Nama field Python `class` tidak valid sebagai atribut biasa.
2. Authentication belum ditentukan di LLD.
3. URL production belum ditentukan.
4. Retensi image reference/hash belum ditentukan.

**Perbaikan:**
- Menggunakan `class_: PlantClass = Field(..., alias="class")`.
- Bearer authentication hanya dicantumkan sebagai opsi/asumsi.
- Production URL menggunakan placeholder.
- Kebijakan retensi ditandai sebagai `[ASUMSI-XX]`.

## Evaluasi kualitas

- Sinkronisasi endpoint dengan LLD: sesuai.
- Sinkronisasi schema OpenAPI dan Pydantic: sesuai.
- ERD hanya menggunakan entitas yang telah ditentukan LLD/HLD.
- Tidak menambahkan endpoint di luar `POST /api/v1/detect`.
