
from pathlib import Path
from PIL import Image
import hashlib
import csv

# Folder dataset mentah
ROOT = Path("dataset_raw")

# Tiga kelas yang digunakan
CLASSES = [
    "Healthy Leaf",
    "Leaf Curl",
    "Spot Leaf",
]

# Format gambar yang diperiksa
EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff"
}

OUTPUT = Path("hasil_audit")
OUTPUT.mkdir(exist_ok=True)

hasil = []
hash_tercatat = {}

for kelas in CLASSES:
    folder = ROOT / kelas

    if not folder.exists():
        print(f"[PERINGATAN] Folder tidak ditemukan: {folder}")
        continue

    jumlah_gambar = 0
    valid = 0
    corrupt = 0
    duplikat = 0

    for file in folder.rglob("*"):
        if not file.is_file():
            continue

        if file.suffix.lower() not in EXTENSIONS:
            continue

        jumlah_gambar += 1
        status = "VALID"
        hash_gambar = ""

        try:
            # Memeriksa apakah file gambar dapat dibaca
            with Image.open(file) as img:
                img.verify()

            # Memastikan gambar dapat dibuka dan didekode
            with Image.open(file) as img:
                img.load()
                img.convert("RGB")

            # Hash untuk menemukan file identik
            hash_gambar = hashlib.sha256(
                file.read_bytes()
            ).hexdigest()

            if hash_gambar in hash_tercatat:
                status = (
                    "DUPLIKAT PERSIS: "
                    + hash_tercatat[hash_gambar]
                )
                duplikat += 1
            else:
                hash_tercatat[hash_gambar] = str(file)
                valid += 1

        except Exception as e:
            status = f"CORRUPT / TIDAK TERBACA: {e}"
            corrupt += 1

        hasil.append({
            "kelas": kelas,
            "file": str(file),
            "status": status,
            "sha256": hash_gambar,
        })

    print(f"\nKelas: {kelas}")
    print(f"Jumlah file gambar : {jumlah_gambar}")
    print(f"File terbaca       : {valid}")
    print(f"File corrupt       : {corrupt}")
    print(f"Duplikat persis    : {duplikat}")

# Simpan hasil pemeriksaan
laporan = OUTPUT / "hasil_audit.csv"

with laporan.open("w", newline="", encoding="utf-8-sig") as f:
    kolom = ["kelas", "file", "status", "sha256"]
    writer = csv.DictWriter(f, fieldnames=kolom)
    writer.writeheader()
    writer.writerows(hasil)

print("\nAudit selesai.")
print(f"Hasil disimpan di: {laporan}")
