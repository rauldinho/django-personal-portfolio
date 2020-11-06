from django.shortcuts import render
from .models import Project

def homepage(request):

    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    
    return render(request, 'portfolio/homepage.html', context)