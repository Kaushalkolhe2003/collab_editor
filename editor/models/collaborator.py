from django.db import models
from django.contrib.auth.models import User
from .document import Document

class Collaborator(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='collaborators')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('editor', 'Editor'), ('viewer', 'Viewer')])

    def __str__(self):
        return f"{self.user.username} - {self.role} of {self.document.title}"
