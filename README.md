# 🌦️ Weather API Proxy

A simple backend application built with **FastAPI** that integrates with the **WeatherAPI** service to retrieve current weather information.

This project demonstrates how to securely consume a third-party API, process the returned data, and expose a clean REST API for clients.

---

## 🚀 Features

- Get current weather by city name
- Asynchronous HTTP requests using `httpx`
- Secure API key management with `.env`
- Input validation using FastAPI
- Error handling for invalid cities and API failures
- Interactive API documentation with Swagger UI

---

## 🛠️ Tech Stack

- Python 3.14
- FastAPI
- Uvicorn
- HTTPX
- Pydantic
- WeatherAPI

---

## 📁 Project Structure

```text
weather-api-proxy/
│
├── app/
│   ├── api/
│   │   ├── router.py
│   │   └── routes/
│   │       └── weather.py
│   │
│   ├── clients/
│   │   └── weather_client.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── schemas/
│   │   ├── common.py
│   │   └── weather.py
│   │
│   ├── services/
│   │   └── weather_service.py
│   │
│   └── main.py
│
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone <repository-url>
cd weather-api-proxy
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
WEATHER_API_KEY=your_api_key
WEATHER_BASE_URL=https://api.weatherapi.com/v1
APP_NAME=Weather API Proxy
DEBUG=True
```

You can get a free API key from:

https://www.weatherapi.com/

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

The application will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 Endpoints

### Health Check

```http
GET /
```

Example Response

```json
{
  "status": "healthy",
  "service": "Weather API Proxy",
  "version": "1.0.0"
}
```

---

### Get Current Weather

```http
GET /weather?city=Cairo
```

Example Response

```json
{
  "city": "Cairo",
  "country": "Egypt",
  "temperature": 34.0,
  "humidity": 42,
  "wind_speed": 14.8,
  "description": "Sunny"
}
```

---

## ❌ Error Responses

### Invalid City

```json
{
  "detail": "City 'UnknownCity' not found."
}
```

### Invalid API Key

```json
{
  "detail": "Invalid Weather API key."
}
```

### Weather Service Unavailable

```json
{
  "detail": "Weather service is unavailable."
}
```

---

## 📚 What I Learned

This project helped me practice:

- Building REST APIs with FastAPI
- Working with third-party APIs
- Asynchronous programming using HTTPX
- Managing environment variables securely
- Validating user input
- Handling HTTP exceptions
- Documenting APIs with Swagger

---

## 👨‍💻 Author

**Hatem Hussein**

Backend Software Engineer