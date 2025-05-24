# Resume Parser Web App

This is a simple Flask-based web application that allows users to upload their resumes in PDF or DOCX format, extracts text content from the files, and parses key details such as name, email, phone number, and skills.

## Features

- Upload resumes in PDF or DOCX format.
- Extract text content from uploaded resumes.
- Parse and display key details including:
  - Name (assumed to be the first line of text)
  - Email address
  - Phone number
  - Skills (basic keyword matching for popular skills)
- Simple web interface with upload and result checking pages.

## Project Structure

Resume Parser Web App/
│
├── templates/
│ ├── upload.html # Upload form for the resume
│ └── check.html # Displays extracted resume details
│
├── uploads/ # Directory to store uploaded files
│
└── app.py # Main Flask application


## Requirements

- Python 3.x
- Flask
- PyPDF2
- python-docx (for docx2txt)
- docx2txt
- Werkzeug

```bash
"pip install Flask PyPDF2 python-docx docx2txt Werkzeug"


# How to Run Resume Parser Web App

This guide explains how to set up and run the Resume Parser Web Application locally.

---

## Prerequisites

- Python 3.x installed on your system
- Basic knowledge of command line usage

---

## Step 1: Clone or Download the Project

Clone the repository or download the project ZIP and extract it.

```bash
git clone <repository-url>
cd Resume-Parser-Web-App
