# 🚀 Pokemon Ability ETL API (FastAPI & PostgreSQL)

Proyek ini adalah sebuah API berbasis **FastAPI** yang mengimplementasikan alur ETL (Extract, Transform, Load). API menerima ID Ability Pokemon, mengambil data dari PokeAPI secara asynchronous, melakukan transformasi data, dan menyimpannya ke database **PostgreSQL**.

---

## 🛠️ Tech Stack
* **Framework:** FastAPI (Python 3.12)
* **Database:** PostgreSQL 15
* **ORM:** SQLAlchemy
* **Containerization:** Docker & Docker Compose
* **Client:** HTTPX (Async API Calls)

---

## 📋 Prasyarat
Sebelum menjalankan, pastikan Anda telah menginstal:
* **Docker Desktop** (untuk Windows dan macOS)
* **Docker Engine & Docker Compose** (untuk Linux/Ubuntu)

---

## 🚀 Cara Menjalankan Project

### 1. Clone github repository
```bash
git clone [https://github.com/dimasguintana/POKEMON-ETL-FASTAPI](https://github.com/dimasguintana/POKEMON-ETL-FASTAPI.git)
cd POKEMON-ETL-FASTAPI
```

### 2. Jalankan dengan Docker Compose
* **Mac / Linux**
```bash
sudo docker compose up --build
```
* **Windows**
```bash
docker compose up --build
```

## Cara Testing
### 1. Dokumentasi Swagger UI
Setelah semua container berjalan (status: `Running`), buka browser dan access: http://localhost:8000/docs.

Apabila mendapatkan seperti di bawah ini:
```bash
web-1  | sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "db" ({host}), port 5432 failed: Connection refused
web-1  |        Is the server running on that host and accepting TCP/IP connections?
```
dan URL docs swagger tidak dapat diakses, anda bisa membuka terminal baru dan eksekusi hal berikut agar bisa berjalan normal:
```bash
docker compose restart web
```

### 2. Mengirim request
* Pilih endpoint `POST /process-ability`
* Klik tombol `Try it out`
* Isi value untuk masing-masing kolom seperti berikut:
```bash
{
    "raw_id": "7dsa8d7sa9dsa",
    "user_id": "5199434",
    "pokemon_ability_id": 150
}
```
* Klik execute
* Jika berhasil, server response akan memberikan code `200` beserta dengan response body.

### 3. Verifikasi data
Gunakan database client untuk memvalidasi data yang sudah masuk ke database dengan menggunakan credential default (dapat diubah di file docker-compose.yml)
* **Host:** `localhost`
* **Port:** `5432`
* **username:** `admin`
* **password:** `admin`

## Struktur Folder Proyek
```bash
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   └── services.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .gitignore
```

## 📝 Fitur & Implementasi
Automated Table Creation: Tabel database otomatis dibuat saat aplikasi dijalankan melalui Base.metadata.create_all di dalam lifespan event.

Asynchronous Processing: Menggunakan async/await dan HTTPX untuk memastikan performa API tetap optimal saat memanggil eksternal API.

Data Transformation: Melakukan filter pada effect_entries dari PokeAPI (hanya mengambil bahasa Inggris) sebelum disimpan ke database.

Containerization: Mengisolasi environment aplikasi dan database sehingga mudah dijalankan di OS mana pun tanpa konflik lokal.