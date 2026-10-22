
import pandas as pd
from pathlib import Path

folder = Path("tweets-data")
file1 = folder / "ubi_bombing.csv"
file2 = folder / "tepung_singkong.csv"

# Baca dan gabungkan kedua CSV
df1 = pd.read_csv(file1, dtype=str, keep_default_na=False)
df2 = pd.read_csv(file2, dtype=str, keep_default_na=False)

print("Data awal ubi_bombing:", len(df1))
print("Data awal tepung_singkong:", len(df2))

gabungan = pd.concat([df1, df2], ignore_index=True)
print("Total sebelum hapus duplikat:", len(gabungan))

# Hapus duplikat berdasarkan ID postingan
gabungan = gabungan.drop_duplicates(
    subset=["id_str"],
    keep="first"
)

print("Total setelah hapus duplikat:", len(gabungan))

# Simpan hasil gabungan tanpa mengubah file asli
output = folder / "gabungan_unik.csv"
gabungan.to_csv(output, index=False, encoding="utf-8-sig")

print("File tersimpan:", output)
