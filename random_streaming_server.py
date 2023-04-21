import cv2
from flask import Flask, render_template, Response
from flask_cors import CORS
import numpy as np
import time
app = Flask(__name__)
CORS(app) 

def generate_frames():
    while True:
        #Generate a random 480x640 RGB image
        frame = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        time.sleep(0.5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

@app.after_request
def apply_caching(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# pip install flask opencv-python-headless
