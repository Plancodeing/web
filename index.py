
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import aspose.words as aw



app=Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('selecttype.html')
@app.route('/home.html')
def upload_form2():
    return render_template('home.html')
 
@app.route('/txt.html')
def upload_form3():
    return render_template('txt.html')
 
@app.route('/md.html')
def upload_form4():
    return render_template('md.html')
 
  
@app.route('/html.html')
def upload_form5():
    return render_template('html.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(filename)
            doc = aw.Document(filename)
            doc.save(filename+".docx")
            os.remove(filename)
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)


@app.route('/txt', methods=['POST'])
def upload_filetxt():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'txtfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['txtfile']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(filename)
            doc = aw.Document(filename)
            doc.save(filename+".txt")
            os.remove(filename)
            flash('converted successfully')
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)



@app.route('/md', methods=['POST'])
def upload_filemd():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'mdfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['mdfile']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(filename)
            doc = aw.Document(filename)
            doc.save(filename+".md")
            os.remove(filename)
            flash('converted successfully')
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)

@app.route('/html', methods=['POST'])
def upload_filehtml():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'htmlfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['htmlfile']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(filename)
            doc = aw.Document(filename)
            doc.save(filename+".html")
            os.remove(filename)
            flash('converted successfully')
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)

if __name__ == "__main__":
    app.run()
