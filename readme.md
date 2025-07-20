# 🚀 Wheel Specification API (FastAPI + PostgreSQL)

This project is a RESTful API built using **FastAPI** and **PostgreSQL** to manage wheel specification forms.

It provides:

-  **POST API** to submit new wheel specifications
-  **GET API** to fetch wheel specifications based on filters

---

## 📂 Project Structure

```
app/
├── main.py          # FastAPI app with POST and GET endpoints
├── models.py        # SQLAlchemy ORM models
├── database.py      # Database connection setup
requirements.txt     # Python dependencies
README.md            # Project documentation
```

---

###  Setup Instructions

###  Clone the Repository

```bash
git clone https://github.com/your-username/wheel-specification-api.git
cd wheel-specification-api
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Configure PostgreSQL

Create a PostgreSQL database and update the `DATABASE_URL` in `database.py`:

```python
DATABASE_URL = "postgresql://<username>:<passwor>d@localhost:<port>/<your_db_name>"
```

## Postgres Setup

```sql
CREATE DATABASE <your_db_name>;
```

## 🚀 Run the API Server

Start the server with:

```bash
uvicorn app.main:app --reload
```

API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

##  API Endpoints

###  POST `/api/forms/wheel-specifications`

Submit a new wheel specification.

- **Request Body (JSON):**

```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "lastShopIssueSize": "837 (800-900)",
    "condemningDia": "825 (800-900)",
    "wheelGauge": "1600 (+2,-1)"
  }
}
```

- **Response:**

```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "status": "Saved"
  }
}
```

---

###  GET `/api/forms/wheel-specifications`

Fetch wheel specifications filtered by `formNumber`, `submittedBy`, and `submittedDate`.

- **Request URL:**

```
http://127.0.0.1:8000/api/forms/wheel-specifications?formNumber=WHEEL-2025-001&submittedBy=user_id_123&submittedDate=2025-07-03
```

- **Response:**

```json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "lastShopIssueSize": "837 (800-900)",
        "condemningDia": "825 (800-900)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ]
}
```

---

##  Tech Stack

-  **Python 3.10+**
-  **FastAPI**
-  **PostgreSQL**
-  **SQLAlchemy**
-  **Uvicorn** (ASGI server)

---

## 🧪 Testing the API

You can test the API using:

- [Postman](https://www.postman.com/)
- [cURL](https://curl.se/)
- Python `requests` library

---

##  Author

- Govind




