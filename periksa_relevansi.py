
import pandas as pd
from pathlib import Path

file_input = Path("tweets-data/gabungan_unik.csv")
df = pd.read_csv(file_input, dtype=str, keep_default_na=False)

# Tampilkan contoh postingan agar relevansinya bisa diperiksa
kolom = ["id_str", "full_text", "tweet_url"]

for i, row in df[kolom].head(30).iterrows():
    print(f"\n--- POSTINGAN {i + 1} ---")
    print("ID:", row["id_str"])
    print("Teks:", row["full_text"].replace("\n", " "))
    print("URL:", row["tweet_url"])
