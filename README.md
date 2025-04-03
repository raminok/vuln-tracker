Edit by: Ramin Orak 3 Apr 2025

# 🐍 Python Application Vulnerability Tracking API

A FastAPI-based application that allows developers to track vulnerabilities in their Python applications' dependencies using the [OSV (Open Source Vulnerability) API](https://osv.dev).

---

## 🚀 Features

- Create and track Python applications.
- Upload `requirements.txt` and identify vulnerable dependencies.
- List all dependencies used across applications.
- View details and vulnerabilities for specific dependencies.
- In-memory storage and response caching for optimal performance.

---

## 🛠️ Technologies

- Python 3.9+
- FastAPI
- Uvicorn
- Cachetools
- Requests

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/raminorak/vuln-tracker.git
cd vuln-tracker

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Our files would be in these folder
app/
├── main.py
├── models.py
└── routes/
    ├── __init__.py  ✅
    ├── applications.py
    └── dependencies.py

