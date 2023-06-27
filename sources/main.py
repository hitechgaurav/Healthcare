from flask import Flask, render_template, request
from models import DetectAI
app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_image', methods=['POST'])
def process_image():
    # Handle image processing logic here based on the uploaded file
    # You can access the uploaded file using request.files['image']
    # Perform necessary operations and return the response
    form_option = request.form['option']
    detection = None
    image = request.files['image'].read()
    detect = DetectAI(image)
    if form_option == 'pneumonia':
        detection = detect.detect_pneumonia()
    else:
        detection = detect.detect_cateract()
    return detection



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5412, debug=True)
