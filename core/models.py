
from django.db import models
from django.urls import reverse

class Internship(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField(help_text="Separate requirements with commas")
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company}"

class Application(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    portfolio_url = models.URLField(blank=True, null=True)
    cover_letter = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ], default='Pending')

    def __str__(self):
        return f"{self.full_name} applied for {self.internship.title}"
