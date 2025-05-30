# ARK10.ai Youtube Downloader v2

This is a Flask-based web application for downloading YouTube videos using . It features a simple UI where users can enter a YouTube video link and view a live progress bar as the video downloads.

## 🚀 Features

- Input field to paste YouTube video URL
- Download button to start the process
- Real-time progress bar using `yt-dlp` hooks
- Backend threading to keep UI responsive
- Uses `yt-dlp` for reliable downloading

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Dependencies:
- Flask
- yt-dlp

## 🛠️ How to Run

```bash
python app.py
```

The app will run on:

```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
ARK10_ai_Youtube_Downloader_v2/
│
├── app.py                 # Flask app
├── templates/
│   └── index.html         # Web interface
├── downloads/             # Downloaded video files (auto-created)
└── requirements.txt       # Python dependencies
```

## 📌 Notes

- For Windows users: use `python app.py` to avoid `SystemExit` from auto-reload issues.
- Ensure you have a stable internet connection for downloading videos.

## 📄 License

This project is open for educational and personal use.
