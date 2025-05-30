# pip install flask yt-dlp


from flask import Flask, render_template, request, jsonify
import yt_dlp
import threading
import os

app = Flask(__name__)
download_progress = {}

def progress_hook(d, video_id):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0.0%').strip().replace('%', '')
        try:
            download_progress[video_id] = float(percent)
        except:
            download_progress[video_id] = 0
    elif d['status'] == 'finished':
        download_progress[video_id] = 100

def download_youtube_video(video_url, video_id):
    ydl_opts = {
        'format': 'best',
        'progress_hooks': [lambda d: progress_hook(d, video_id)],
        'outtmpl': f'downloads/{video_id}.%(ext)s'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception:
        download_progress[video_id] = -1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    video_url = data.get('link')
    video_id = str(hash(video_url))
    threading.Thread(target=download_youtube_video, args=(video_url, video_id)).start()
    return jsonify({'video_id': video_id})

@app.route('/progress/<video_id>')
def progress(video_id):
    progress = download_progress.get(video_id, 0)
    return jsonify({'progress': progress})

if __name__ == '__main__':
    os.makedirs("downloads", exist_ok=True)
    app.run(debug=True, use_reloader=False)
