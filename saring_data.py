
import pandas as pd
from pathlib import Path

folder = Path("tweets-data")
input_file = folder / "gabungan_unik.csv"

df = pd.read_csv(input_file, dtype=str, keep_default_na=False)

# Kata/frasa yang menunjukkan kemungkinan topik makanan lain
kata_tidak_relevan = [
    "tempe mendoan",
    "sayur singkong",
    "daun singkong",
    "tumis singkong",
    "resep singkong",
    "keripik singkong",
    "goreng singkong",
    "olklahoma city bombing",
    "oklahoma city bombing",
    "israel bombing",
    "uss liberty",
    "jfk assassination",
    "epstein",
    "covid-19",
]

teks = df["full_text"].str.lower()

# Tandai postingan yang mengandung frasa di atas
mask = teks.apply(
    lambda t: any(kata in t for kata in kata_tidak_relevan)
)

df["status_saringan"] = "Perlu diperiksa"
df.loc[mask, "status_saringan"] = "Kemungkinan tidak relevan"

# Simpan semua data beserta tanda saringannya
output = folder / "hasil_saringan_awal.csv"
df.to_csv(output, index=False, encoding="utf-8-sig")

print("Total postingan:", len(df))
print("Kemungkinan tidak relevan:", int(mask.sum()))
print("Perlu diperiksa:", int((~mask).sum()))
print("Hasil disimpan di:", output)
