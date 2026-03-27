from django.shortcuts import get_object_or_404, render
from .models import Project, Tag

# This file is effectively the controller in the MVC architecture.
# It handles the logic of fetching data from the database and rendering the appropriate templates.

def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, 'projects.html', {'projects': projects, 'tags': tags})

def contact(request):
    return render(request, 'contact.html')

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})
