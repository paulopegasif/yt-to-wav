# 🎵 YouTube to WAV Converter

A minimalistic web application that allows you to **download high-quality WAV audio** from YouTube videos. Built with a modern and clean **Notion-inspired** interface, the project supports **Portuguese 🇧🇷, English 🇺🇸, and Spanish 🇪🇸**.

## 🌟 Features

- Download **WAV audio** from any YouTube video.
- **Responsive UI** with Tailwind CSS, inspired by Notion.
- **Multilingual** support (PT, EN, ES) with a simple language switcher.
- **Progress bar** while processing the download.

---

## 🛠️ Technologies

- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Backend:** Python, FastAPI, yt-dlp

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/yt-to-wav.git
cd yt-to-wav
```

### 2. Backend Setup (FastAPI)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The backend runs on `http://localhost:8000`.

Make sure **yt-dlp** is installed on your system:

```bash
brew install yt-dlp  # (For macOS users)
```

### 3. Frontend Setup

- Open `frontend/index.html` in your browser.

---

## 🌐 Deployment

### 1. Frontend Deployment (Vercel)

- Go to [Vercel](https://vercel.com/).
- Import the **frontend/** folder as a new project.
- Deploy directly with default settings.

### 2. Backend Deployment (Railway or Render)

- Go to [Railway](https://railway.app/) or [Render](https://render.com/).
- Create a new Python project and connect the **backend/** folder.
- Ensure **yt-dlp** is installed in the environment (add it to the build or startup commands).

### 3. Update Frontend API URL

- In `frontend/index.html`, replace:

```javascript
fetch('http://localhost:8000/download')
```

with your deployed backend URL, like:

```javascript
fetch('https://your-backend-url/download')
```

---

## 📄 License

This project is licensed under the MIT License.

---

Feel free to customize, contribute, or reach out for any improvements! 🚀🎧