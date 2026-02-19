from django.db import models
from django.conf import settings

class Project(models.Model):
    STATUS_CHOICES = ( 
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_projects'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    required_skills = models.ManyToManyField('users.Skill', blank=True)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='proposals')
    freelancer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='freelancer_proposals'
    )
    cover_letter = models.TextField()
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_duration = models.CharField(max_length=50)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.freelancer.username} proposal for {self.project.title}"
