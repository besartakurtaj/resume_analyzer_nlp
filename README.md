# Resume analyzer NLP (Django Web App)

A web-based application built with Django and NLP techniques to analyze resumes against job descriptions and compute a skill-matching score.

## Tech Stack:

Backend: Python, Django
Frontend: HTML, Bootstrap (via Django templates)
NLP: NLTK
PDF Parsing: PyPDF2
Database: SQLite (default)
## Project Structure:

![image](https://github.com/user-attachments/assets/fc024093-a860-47c6-9f8b-f5767eedf622)


## How It Works

1. User uploads a resume PDF and pastes a job description.
2. The system:
     - Extracts text from the PDF using PyPDF2
     - Tokenizes and cleans text using NLTK
     - Compares skill sets from resume and job description
3. Outputs a match score and lists matched skills.

## Setup Instructions

### 1. Clone the Repo
   git clone https://github.com/besartakurtaj/resume_analyzer_nlp.git
   cd resume-analyzer-nlp

### 2. Download NLTK Data (once)
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

#### 3. Run Migrations
   python manage.py migrate

#### 4. Start the Server
  python manage.py runserver

## Contributing
Contributions are welcome!
Feel free to open issues, suggest features, or submit pull requests.


   

