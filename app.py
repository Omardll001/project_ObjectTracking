from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'message': 'No video file provided'}), 400
    
    video = request.files['video']
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)
    
    # Here you can call your AI model to process the video
    # For now, we'll just return a success message
    return jsonify({'message': 'Video uploaded successfully', 'video_path': video_path})

if __name__ == '__main__':
    app.run(debug=True)
