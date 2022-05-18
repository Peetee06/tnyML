from http.client import NO_CONTENT
import time
import os
from tkinter.messagebox import RETRY
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash;
from flask_cors import CORS, cross_origin;
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'public/user/uploads/'
ALLOWED_EXTENSIONS = {'bmp', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
cors =CORS(app,resources={r'/api/*':{'origins':'http://localhost:4200'}})
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


data = [
    {
        "day": "1/6/2019",
    },
    {
        "day": "2/6/2019",
    }
]

# all around data upload
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/api/uploadfile/", methods = ['GET', 'POST'])
@cross_origin(supports_credentials=True)
def uploadFile():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded successfully'
# end upload section

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

@app.route("/", methods=['GET'])
def index():
    context = { 'server_time': format_server_time() }
    return render_template('index.html', context=context)

@app.route("/api/getData/", methods = ['GET'])
def getData():
    global data
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True,port=int(os.environ.get('PORT', 5000)))