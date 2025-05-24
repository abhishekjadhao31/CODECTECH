from flask import Flask, render_template, request, redirect, url_for, session
import os
import docx2txt
import PyPDF2
import re
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Make sure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(filepath):
    ext = filepath.rsplit('.', 1)[1].lower()
    text = ''
    if ext == 'pdf':
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ''
    elif ext == 'docx':
        text = docx2txt.process(filepath)
    return text.strip()

def extract_details(text):
    # Email
    email = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email = email.group(0) if email else 'Not found'

    # Phone number (basic formats)
    phone = re.search(r'\+?\d[\d\s\-()]{8,}\d', text)
    phone = phone.group(0) if phone else 'Not found'

    # Name (first non-empty line, assuming it's the top)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    name = lines[0] if lines and len(lines[0].split()) <= 5 else 'Not found'

    # Skills (basic keyword match)
    skills_keywords = ['python', 'java', 'c++', 'sql', 'excel', 'communication', 'teamwork', 'ml', 'flask']
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    skills = ', '.join(found_skills) if found_skills else 'Not found'

    return {
        'Name': name,
        'Email': email,
        'Phone': phone,
        'Skills': skills
    }

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return 'No file part'
    file = request.files['resume']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        text = extract_text_from_file(filepath)
        session['resume_text'] = text
        return redirect(url_for('check_resume'))
    else:
        return 'Invalid file type. Please upload a PDF or DOCX.'

@app.route('/check')
def check_resume():
    resume_text = session.get('resume_text', 'No resume uploaded yet.')
    details = extract_details(resume_text)
    return render_template('check.html', resume_text=resume_text, details=details)

if __name__ == '__main__':
    app.run(debug=True)
