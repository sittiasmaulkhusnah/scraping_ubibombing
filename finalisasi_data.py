
import pandas as pd
from pathlib import Path

folder = Path("tweets-data")
df = pd.read_csv(
    folder / "hasil_saringan_awal.csv",
    dtype=str,
    keep_default_na=False
)

relevan = df[df["status_saringan"] == "Perlu diperiksa"].copy()
periksa = df[df["status_saringan"] == "Kemungkinan tidak relevan"].copy()

relevan.to_csv(
    folder / "kandidat_relevan.csv",
    index=False,
    encoding="utf-8-sig"
)

periksa.to_csv(
    folder / "perlu_dikeluarkan.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Kandidat untuk pemeriksaan relevansi:", len(relevan))
print("Postingan untuk diperiksa/dikeluarkan:", len(periksa))
print("File kandidat: tweets-data/kandidat_relevan.csv")
print("File pemeriksaan: tweets-data/perlu_dikeluarkan.csv")
