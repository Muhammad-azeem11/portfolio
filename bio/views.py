from django.shortcuts import render
from .models import Bio
from education.models import Education
from experience.models import Experience 
from projects.models import Project
from skills.models import Skill

def home(request):
    context = {
        'bio': Bio.objects.first(),
        'education': Education.objects.all(),
        'experience': Experience.objects.all(),
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
    }
    return render(request, 'index.html', context)