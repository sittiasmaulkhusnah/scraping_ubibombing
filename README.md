# Scraping Data X: Ubi Bombing, Tepung Singkong, dan Karhutla

## 1. Deskripsi Proyek

Proyek ini berfokus pada pengumpulan data postingan dari platform X (sebelumnya Twitter) yang membahas topik ubi bombing, yaitu wacana penggunaan tepung singkong untuk membantu memadamkan kebakaran hutan dan lahan (karhutla).

Pengumpulan data dilakukan menggunakan teknik web scraping dengan bantuan Tweet-Harvest. Pada proses awal, kata kunci ubi bombing digunakan untuk memperoleh postingan yang relevan dengan topik. Namun, jumlah data yang diperoleh dari kata kunci tersebut belum mencukupi target minimal 1.000 baris. Oleh karena itu, ditambahkan kata kunci tepung singkong dan karhutla untuk memperluas cakupan pencarian dan memperoleh data tambahan yang masih berkaitan dengan topik.

Data yang terkumpul kemudian digabungkan dan menjalani penyaringan awal serta pemeriksaan kualitas sebelum disimpan dalam dataset berformat CSV.

## 2. Tujuan

Tujuan proyek ini adalah:

- Mengumpulkan postingan X berdasarkan kata kunci yang berkaitan dengan topik penelitian.
- Menggabungkan data dari beberapa kata kunci ke dalam satu dataset.
- Melakukan penyaringan awal untuk mengidentifikasi postingan yang kemungkinan tidak relevan.
- Memeriksa kelengkapan data dan duplikasi berdasarkan ID postingan.

## 3. Tools dan Teknologi

Tools yang digunakan dalam proyek ini meliputi:

- **Node.js** — menjalankan proses scraping.
- **Tweet-Harvest** — membantu mengambil data postingan X.
- **Python** — melakukan penggabungan, penyaringan, dan pemeriksaan data.
- **pandas** — mengolah dataset dalam format CSV.
- **Visual Studio Code** — lingkungan pengembangan untuk menjalankan skrip dan mengelola file proyek.

## 4. Kata Kunci Scraping

Pengumpulan data dilakukan menggunakan tiga kata kunci:
1. ubi bombing, kata kunci utama untuk mencari postingan yang secara langsung membahas topik ubi bombing.
2. tepung singkong, kata kunci tambahan karena jumlah data dari kata kunci utama belum mencapai target minimal 1.000 baris.
3. karhutla, kata kunci tambahan untuk memperluas pengumpulan data terkait kebakaran hutan dan lahan serta melengkapi jumlah data yang dibutuhkan.
Penggunaan beberapa kata kunci bertujuan memperluas cakupan pencarian agar jumlah data yang dikumpulkan memenuhi target tugas. Data dari setiap kata kunci disimpan dalam file CSV tersendiri sebelum digabungkan dan diproses lebih lanjut.

Setiap kata kunci menghasilkan file CSV tersendiri sebelum data digabungkan.

## 5. Proses Pengumpulan dan Pengolahan Data

Proses pengerjaan dilakukan melalui beberapa tahapan berikut:

1. **Scraping data**  
   Mengumpulkan postingan dari platform X menggunakan Tweet-Harvest berdasarkan tiga kata kunci: `ubi bombing`, `tepung singkong`, dan `karhutla`. Kata kunci tambahan digunakan karena hasil pencarian awal belum memenuhi target minimal 1.000 baris data.

2. **Penggabungan data awal**  
   Menggabungkan hasil scraping dari kata kunci `ubi bombing` dan `tepung singkong` ke dalam satu dataset.

3. **Penyaringan awal data**  
   Melakukan penyaringan menggunakan Python untuk menandai postingan yang kemungkinan tidak relevan berdasarkan daftar kata atau frasa tertentu, seperti pembahasan resep makanan berbahan singkong dan topik pengeboman lain yang tidak berkaitan dengan ubi bombing.

4. **Pemisahan kandidat data**  
   Memisahkan data menjadi kandidat yang perlu diperiksa lebih lanjut dan data yang terindikasi tidak relevan berdasarkan aturan penyaringan. Proses ini merupakan penyaringan otomatis, bukan verifikasi relevansi secara manual.

5. **Pengambilan data tambahan**  
   Melakukan scraping menggunakan kata kunci `karhutla` untuk menambah jumlah postingan dan memperluas cakupan data terkait kebakaran hutan dan lahan.

6. **Penggabungan dataset akhir**  
   Menggabungkan 775 baris kandidat dari hasil penyaringan dua kata kunci awal dengan 300 baris hasil scraping `karhutla`. Penggabungan menghasilkan 1.075 baris data tanpa ID postingan duplikat.

7. **Pemeriksaan kualitas data**  
   Memeriksa jumlah baris, kelengkapan ID, teks, dan tanggal postingan, serta duplikasi ID menggunakan pandas.

## 6. Hasil Scraping

Dataset gabungan akhir berisi **1.075 baris data** dengan 16 kolom.

Pemeriksaan teknis menghasilkan temuan berikut:

| Pemeriksaan              | Hasil |
| ------------------------ | ----: |
| Jumlah baris             | 1.075 |
| Jumlah kolom             |    16 |
| ID postingan kosong      |     0 |
| ID postingan duplikat    |     0 |
| Teks postingan kosong    |     0 |
| Tanggal postingan kosong |     0 |

Kolom dataset mencakup informasi seperti tanggal postingan, teks, bahasa, jumlah suka, jumlah balasan, jumlah repost, URL postingan, identitas akun, serta status penyaringan.

File dataset utama: `gabungan_3keywords.csv`

## 7. Struktur Folder

Struktur file utama proyek:


scraping_ubibombing/
├── README.md
├── .gitignore
├── package-lock.json
├── pnpm-workspace.yaml
│
├── bersihkan_data.py
├── finalisasi_data.py
├── gabungkan_keyword3.py
├── periksa_relevansi.py
├── saring_data.py
├── saring_keyword3.py
│
└── tweets-data/
    ├── ubi_bombing.csv
    ├── tepung_singkong.csv
    ├── karhutla.csv
    ├── hasil_saringan_2keywords.csv
    └── gabungan_3keywords.csv

Nama dan lokasi file pada struktur di atas mengikuti susunan yang digunakan selama pengerjaan. File yang tidak tersedia atau memiliki nama berbeda perlu disesuaikan dengan kondisi repository.

## 8. Cara Menjalankan

Bagian ini menjelaskan cara menyiapkan lingkungan kerja, menjalankan proses scraping, dan memeriksa dataset menggunakan skrip yang tersedia dalam repository.

### A. Persiapan lingkungan

Pastikan Node.js dan Python telah terpasang. Buka terminal pada folder proyek, kemudian instal dependensi Python yang diperlukan:

```bash
pip install pandas
```

Dependensi Node.js perlu disiapkan sesuai konfigurasi `package.json` dan petunjuk instalasi Tweet-Harvest yang digunakan.

### B. Menjalankan scraping

Scraping dilakukan dengan menjalankan perintah Tweet-Harvest melalui terminal. Contoh berikut digunakan untuk mengambil postingan terbaru berdasarkan kata kunci `karhutla` dengan batas 300 postingan:

```bash
node dist/bin.js -t "<TOKEN_X>" -s "karhutla" -l 300 --tab LATEST -o "keyword3_karhutla" -e csv
```

Keterangan parameter:
- `-t`: token autentikasi yang diperlukan oleh tool.
- `-s`: kata kunci pencarian.
- `-l`: batas jumlah postingan yang ingin diambil.
- `--tab LATEST`: menggunakan tab hasil pencarian terbaru.
- `-o`: nama output.
- `-e csv`: menyimpan hasil dalam format CSV.

Token autentikasi harus disediakan secara lokal dan tidak boleh diunggah ke repository publik.

### C. Menjalankan pengolahan data

Skrip Python digunakan untuk menggabungkan data, melakukan penyaringan awal, dan memeriksa kualitas dataset. Jalankan skrip sesuai urutan proses dan nama file yang tersedia dalam repository.

Contoh pemeriksaan dataset menggunakan pandas:

```python
import pandas as pd

df = pd.read_csv("tweets-data/gabungan_3keywords.csv", dtype=str)

print("Jumlah baris dan kolom:", df.shape)
print("ID kosong:", df["id_str"].isna().sum())
print("ID duplikat:", df["id_str"].duplicated().sum())
print("Teks kosong:", df["full_text"].isna().sum())
print("Tanggal kosong:", df["created_at"].isna().sum())
```

Perintah dan nama skrip perlu disesuaikan dengan struktur file yang tersedia. Jika hanya ingin melihat hasil akhir, dataset `gabungan_3keywords.csv` dapat langsung dibuka menggunakan aplikasi spreadsheet atau Python tanpa menjalankan ulang scraping.

## 9. Catatan dan Keterbatasan

- Data dikumpulkan berdasarkan kata kunci sehingga hasilnya bergantung pada ketersediaan dan respons pencarian di X ketika scraping dilakukan.
- Penyaringan dilakukan secara otomatis berdasarkan kata atau frasa tertentu. Karena itu, hasil penyaringan awal belum menjamin seluruh postingan relevan dengan topik.
- Data perlu ditinjau lebih lanjut apabila akan digunakan untuk analisis yang memerlukan relevansi kontekstual.
- Kode bahasa yang terdeteksi pada dataset tidak seluruhnya menunjukkan bahasa Indonesia atau Inggris.
- Hasil scraping merupakan data yang dikumpulkan pada saat pengerjaan dan dapat berbeda apabila proses dijalankan kembali.

## 10. Penutup

Proyek ini menghasilkan dataset gabungan dari tiga kata kunci yang berkaitan dengan ubi bombing, tepung singkong, dan karhutla. Dataset beserta skrip pengolahan dan dokumentasi disiapkan sebagai bukti proses pengerjaan tugas web scraping.
