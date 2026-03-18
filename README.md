# 🚀 Pokemon Ability ETL API (FastAPI & PostgreSQL)

This project is a **FastAPI**-based application that implements a robust ETL (Extract, Transform, Load) pipeline. The API consumes Pokemon Ability IDs, fetches data asynchronously from the PokeAPI, performs data transformation (filtering and normalization), and persists the results into a **PostgreSQL** database.

---

## 🛠️ Tech Stack
* **Framework:** FastAPI (Python 3.12)
* **Database:** PostgreSQL 15
* **ORM:** SQLAlchemy
* **Containerization:** Docker & Docker Compose
* **HTTP Client:** HTTPX (Asynchronous API Calls)

---

## 📋 Prerequisites
Ensure you have the following installed on your system:
* **Docker Desktop** (for Windows and macOS)
* **Docker Engine & Docker Compose** (for Linux/Ubuntu)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/dimasguintana/POKEMON-ETL-FASTAPI.git](https://github.com/dimasguintana/POKEMON-ETL-FASTAPI.git)
cd POKEMON-ETL-FASTAPI
```

### 2. Run with Docker Compose
* **Mac / Linux**
```bash
sudo docker compose up --build
```
* **Windows**
```bash
docker compose up --build
```

## Testing & Verification
### 1. API Documentation (Swagger UI)
Once all containers are up and running, access the interactive documentation at:
👉 http://localhost:8000/docs

Troubleshooting: Connection Refused
If you encounter a sqlalchemy.exc.OperationalError (Connection refused) during the first startup, it means the web service attempted to connect before the database was fully initialized. To resolve this, simply restart the web container:

```bash
docker compose restart web
```

### 2. Executing the ETL Process
* Locate the POST /process-ability endpoint.

* Click "Try it out".

* Use the following JSON payload as an example:
```bash
{
    "raw_id": "7dsa8d7sa9dsa",
    "user_id": "5199434",
    "pokemon_ability_id": 150
}
```
* Click Execute. A successful process will return a 200 OK status code with the processed data in the response body.

### 3. Database verification
You can verify the persisted data using any database client (e.g., DBeaver, TablePlus, or pgAdmin) with the following default credentials (can be change in docker-compose.yml file):
* **Host:** `localhost`
* **Port:** `5432`
* **username:** `admin`
* **password:** `admin`

## Project Structure
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
* **Automated Schema Migration**: Database tables are automatically generated upon application startup using Base.metadata.create_all within the FastAPI lifespan event.

* **Asynchronous Concurrency**: Leverages async/await and HTTPX to ensure non-blocking I/O operations when fetching data from external APIs.

* **Data Transformation**: Implements server-side filtering on PokeAPI effect_entries to extract only English descriptions before storage.

* **Full Containerization**: Decouples the application and database environments, ensuring seamless deployment across different operating systems without local dependency conflicts.