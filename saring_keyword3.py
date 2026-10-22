
import pandas as pd
from pathlib import Path

folder = Path("tweets-data")

input_file = folder / "keyword3_karhutla.csv"
output_file = folder / "hasil_saringan_keyword3.csv"

df = pd.read_csv(input_file, dtype=str, keep_default_na=False)

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

mask = teks.apply(
    lambda t: any(kata in t for kata in kata_tidak_relevan)
)

df["status_saringan"] = "Perlu diperiksa"
df.loc[mask, "status_saringan"] = "Kemungkinan tidak relevan"

df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("Total postingan keyword 3:", len(df))
print("Kemungkinan tidak relevan:", int(mask.sum()))
print("Perlu diperiksa:", int((~mask).sum()))
print("Hasil disimpan di:", output_file)
