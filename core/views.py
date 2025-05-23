from django.shortcuts import render
from .models import Resume, JobDescription, MatchResult
from .utils import extract_skills, compute_score
from PyPDF2 import PdfReader


def index(request):
    if request.method == 'POST':
        resume_file = request.FILES['resume']
        jobdesc_text = request.POST['jobdesc']

        resume = Resume.objects.create(file = resume_file)
        jd = JobDescription.objects.create(content=jobdesc_text)

        text = ''
        if resume_file.name.endswith('.pdf'):
            reader = PdfReader(resume_file)
            text = ''.join(page.extract_text() for page in reader.pages if page.extract_text())

        resume_skills = extract_skills(text)
        jd_skills = extract_skills(jobdesc_text)

        score, matched = compute_score(resume_skills, jd_skills)
        result = MatchResult.objects.create(
            resume = resume,
            job_description = jd,
            score = score,
            skills_matched = ', '.join(matched)
        )

        return render(request, '../templates/result.html', {
            'score' : score,
            'skills': matched
        })
    
    return render(request, '../templates/index.html')