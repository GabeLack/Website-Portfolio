from django.db import models


# Tag model to categorize projects
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Project model to represent each project in the portfolio
class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True, default='')
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='projects')
    link = models.URLField(blank=True, max_length=200)
    pdf = models.FileField(upload_to='project_pdfs/', blank=True, null=True)

    def __str__(self):
        return self.title


# ProjectImage model to store images related to each project
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE
        )
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.title}"