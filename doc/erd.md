# ERD AgriScan AI

```mermaid
erDiagram
    EVALUATION_RUN ||--o{ REAL_WORLD_TEST : "memiliki"
    EVALUATION_RUN ||--o{ CLASS_METRIC : "memiliki"

    PREDICTION_LOG {
        UUID prediction_id PK
        DATETIME created_at "NOT NULL"
        STRING predicted_class "NOT NULL"
        FLOAT confidence "NOT NULL 0..1"
        STRING status "NOT NULL"
        BOOLEAN is_ood "NOT NULL"
        INTEGER processing_time_ms "NOT NULL"
        STRING model_version "NOT NULL"
        STRING image_hash "NULL"
    }

    EVALUATION_RUN {
        UUID evaluation_id PK
        STRING evaluation_type "NOT NULL"
        DATETIME started_at "NOT NULL"
        DATETIME completed_at "NULL"
        INTEGER sample_count "NOT NULL"
        FLOAT accuracy "NULL 0..1"
    }

    REAL_WORLD_TEST {
        UUID sample_id PK
        UUID evaluation_id FK
        INTEGER sample_number "NOT NULL"
        STRING actual_class "NOT NULL"
        STRING predicted_class "NOT NULL"
        FLOAT confidence "NOT NULL 0..1"
        BOOLEAN is_correct "NOT NULL"
        STRING image_reference "NULL"
        DATETIME tested_at "NOT NULL"
    }

    CLASS_METRIC {
        UUID metric_id PK
        UUID evaluation_id FK
        STRING class_name "NOT NULL"
        FLOAT precision "NOT NULL 0..1"
        FLOAT recall "NOT NULL 0..1"
        FLOAT f1_score "NOT NULL 0..1"
        INTEGER support "NOT NULL"
    }
```

## Index dan constraint penting

- `prediction_log`: PK `prediction_id`; index `created_at`, `predicted_class`, `image_hash`.
- `evaluation_run`: PK `evaluation_id`; index `evaluation_type`.
- `real_world_test`: PK `sample_id`; FK `evaluation_id`; unique `(evaluation_id, sample_number)`.
- `class_metric`: PK `metric_id`; FK `evaluation_id`; unique `(evaluation_id, class_name)`.
- Confidence dan metric bernilai 0–1.
- Accuracy bernilai 0–1.
- `sample_number >= 1`.
- Real-world evaluation minimal 60 sampel divalidasi pada application/service layer.
- Enam kelas: Cabai Normal, Cabai Antraknosa, Cabai Leaf Curl, Tomat Normal, Tomat Early Blight, Tomat Late Blight.

# [ASUMSI-03]
`image_reference` hanya menyimpan path/URL sementara; kebijakan retensi file belum ditentukan.
