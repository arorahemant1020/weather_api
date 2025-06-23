# 🌦️ WeatherWave - Real-Time Weather API

WeatherWave is a real-time weather data API built using **Django**, with WebSocket support powered by **Django Channels** and **Redis**. It integrates with the OpenWeatherMap API to fetch live weather data by city name and returns temperature, humidity, and condition descriptions.

---

## 🚀 Features

* 🔍 Get current weather by city name (via REST API)
* ⚡ Real-time weather updates using WebSockets
* 🔗 Integration with [OpenWeatherMap](https://openweathermap.org/)
* 🐘 PostgreSQL database
* 🔴 Redis for WebSocket channel layers

---

## 🧰 Tech Stack

| Layer        | Technology                    |
| ------------ | ----------------------------- |
| Backend      | Django, Django REST Framework |
| Realtime     | Django Channels + Redis       |
| Database     | PostgreSQL                    |
| External API | OpenWeatherMap API            |
| Language     | Python                        |

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/weatherwave.git
cd weatherwave
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL

Create a PostgreSQL database and user:

```sql
CREATE DATABASE weatherproj_db;
CREATE USER weatherapi WITH PASSWORD '1234';
GRANT ALL ON SCHEMA public TO weatherapi;
```

Update your `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'weatherproj_db',
        'USER': 'weatherapi',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Add OpenWeatherMap API Key

Get a free API key from [OpenWeatherMap](https://openweathermap.org/api) and add it in `settings.py`:

```python
OPENWEATHER_API_KEY = 'your_api_key_here'
```

### 6️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ Start Redis Server

```bash
redis-server
```

If you're on Windows and Redis is already running, skip this step.

### 8️⃣ Run Development Server

```bash
python manage.py runserver
```

---

## 🌐 API Usage

### 🔁 REST API

**Base URL:** `http://127.0.0.1:8000/api/`

| Endpoint           | Method | Description              |
| ------------------ | ------ | ------------------------ |
| `/weather/<city>/` | GET    | Get weather info by city |

**Example:**

```http
GET /api/weather/New%20York/
```

**Response:**

```json
{
  "city": "New York",
  "temperature": 27.3,
  "humidity": 52,
  "description": "clear sky"
}
```

---

### 🔌 WebSocket API

**URL:** `ws://127.0.0.1:8000/ws/weather/`

**Client Sends:**

```json
{ "city": "Delhi" }
```

**Server Responds:**

```json
{
  "city": "Delhi",
  "temperature": 32.4,
  "humidity": 58,
  "description": "haze"
}
```

---

## 🛠️ Project Structure

```
weather_proj/
├── weatherwave/         # Project settings
│   ├── settings.py
│   ├── asgi.py
│   └── urls.py
│   └── wsig.py
├── weather/             # App for weather logic
│   ├── views.py
│   ├── utils.py
│   ├── consumers.py
│   ├── routing.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📜 API Summary

### Base URL

```
http://127.0.0.1:8000/api/
```

### REST Endpoint

```
GET /api/weather/<city>/
Example: /api/weather/Delhi/
```

### WebSocket Endpoint

```
ws://127.0.0.1:8000/ws/weather/
Send: { "city": "New York" }
```

---


## 🙋‍♂️ Author

**Hemant Arora**
Feel free to connect for collaboration, improvements, or feedback.
