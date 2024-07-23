import os
import subprocess
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from utils.video_utils import read_video, save_video
from trackers.tracker import Tracker

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output_videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return redirect(url_for('processing', filename=file.filename))

@app.route('/processing/<filename>')
def processing(filename):
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_video_path = os.path.join(app.config['OUTPUT_FOLDER'], f'processed_{filename}')
    
    # Call the main.py script to process the video
    result = subprocess.run(['python', 'main.py', video_path, output_video_path], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error processing video: {result.stderr}")
        return redirect(url_for('error'))

    return redirect(url_for('result', filename=f'processed_{filename}'))

@app.route('/result/<filename>')
def result(filename):
    return render_template('result.html', filename=filename)

@app.route('/output_videos/<filename>')
def send_video(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

@app.route('/error')
def error():
    return "An error occurred while processing the video."

if __name__ == '__main__':
    app.run(debug=True)
