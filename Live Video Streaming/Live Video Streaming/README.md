# Live Video Streaming with Python and Flask

This project demonstrates **Live Video Streaming using Python**, **Flask**, and **Gunicorn** with **gevent** for asynchronous handling. It captures video using OpenCV, streams it live over the web, and saves the streamed video locally.

\ud83d\udd27 Developed by: **Abhishek Jadhav**
\ud83c\udfa5 Demo: See `video.mkv` for a working example.
\ud83d\udccb Inspired by the article written by **Miguel Grinberg**

---

## \ud83d\udd27 Dependencies

Install the following Python packages before running the project:

```bash
pip3 install opencv-python	
pip3 install flask
pip3 install gunicorn      # Not supported on Windows
pip3 install gevent        # Not supported on Windows
```

---

## \ud83d\ude80 Running the Application

### \u2705 Ubuntu/Linux

#### \ud83d\udd39 Without Gunicorn:

```bash
export FLASK_APP=livefeed.py
flask run
```

#### \ud83d\udd39 With Gunicorn:

```bash
gunicorn --threads 5 --workers 1 --bind 0.0.0.0:5000 livefeed:app
```

#### \ud83d\udd39 With Gunicorn + Gevent (Asynchronous support):

```bash
gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:5000 livefeed:app
```

---

### \ud83e\uddcf\u200d\u2642\ufe0f Windows

Gunicorn and gevent are not supported. Use this instead:

```bash
python3 livefeed.py
```

---

## \ud83c\udf10 Port Forwarding for Public Access

### \u2705 Ubuntu/Linux (using ngrok)

1. Download and install **ngrok** from [https://ngrok.com/](https://ngrok.com/).
2. In the terminal, run:

```bash
./ngrok http http://127.0.0.1:5000/ --bind-tls true
```

> Replace `5000` with your Flask port if different.

---

### \ud83e\uddcf\u200d\u2642\ufe0f Windows (using Flask-Ngrok)

1. Install the ngrok wrapper:

```bash
pip install flask-ngrok
```

2. Add the following to your `livefeed.py` before `app.run()`:

```python
from flask_ngrok import run_with_ngrok
run_with_ngrok(app)
```

---

## \ud83d\udcc2 Folder Structure (Example)

```
.
├── livefeed.py         # Main Flask app
├── video.mkv           # Demo video of streaming
├── README.md           # This file
```

---

## \ud83d\udccc Notes

* Make sure your webcam is accessible by OpenCV.
* Use Gunicorn and gevent for better performance on production.
* ngrok gives you a public URL to access your stream anywhere.

---

## \ud83d\udce9 Author

**Abhishek Jadhav**

Feel free to reach out for contributions or questions!
