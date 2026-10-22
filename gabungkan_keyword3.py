
import pandas as pd
from pathlib import Path

folder = Path("tweets-data")

file_lama = folder / "kandidat_relevan.csv"
file_baru = folder / "keyword3_karhutla.csv"
file_output = folder / "gabungan_kandidat_keyword3.csv"

lama = pd.read_csv(file_lama, dtype=str, keep_default_na=False)
baru = pd.read_csv(file_baru, dtype=str, keep_default_na=False)

gabungan = pd.concat([lama, baru], ignore_index=True)

jumlah_awal = len(gabungan)

if "id_str" not in gabungan.columns:
    raise ValueError("Kolom id_str tidak ditemukan.")

gabungan = gabungan.drop_duplicates(
    subset=["id_str"],
    keep="first"
)

gabungan.to_csv(
    file_output,
    index=False,
    encoding="utf-8-sig"
)

print("Kandidat lama:", len(lama))
print("Hasil keyword 3:", len(baru))
print("Total sebelum deduplikasi:", jumlah_awal)
print("Total setelah deduplikasi:", len(gabungan))
print("Duplikat dihapus:", jumlah_awal - len(gabungan))
print("File tersimpan:", file_output)
