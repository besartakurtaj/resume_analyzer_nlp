from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='resume/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class JobDescription(models.Model):
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MatchResult(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    score = models.FloatField()
    skills_matched = models.TextField()
