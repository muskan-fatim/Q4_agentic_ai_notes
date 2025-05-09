# 🌐 FastAPI Greeting App

This is a minimal FastAPI application that serves a single GET endpoint to return a greeting message.

## 🚀 Endpoint

### `GET /`

Returns a JSON greeting message.

#### Response:
```json
{
  "message": "Hello beautiful"
}
````

## 📦 Requirements

* Python 3.7+
* FastAPI
* Uvicorn (for running the server)

## 🔧 Installation

1. Clone the repository or copy the `main.py` file.

2. Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install fastapi
```

## ▶️ Running the App

Start the server with:

```bash
fastapi dev main.py
```

Then visit `http://127.0.0.1:8000` in your browser or use a tool like Postman.

## 📚 Auto Docs

FastAPI provides interactive API docs out of the box:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## ✨ Example Output

```bash
curl http://127.0.0.1:8000/

# Output:
# {"message": "Hello beautiful"}
```

---

Built with 💖 using FastAPI.
