from django.shortcuts import render
from main.models import Skill, Message, Project, Biography, Secsub, Contact, Home
from django.http import HttpResponseRedirect
# Create your views here.


def main(request):
    skills = Skill.objects.all() #queryset orm

    project = Project.objects.all()
    biography = Biography.objects.all()
    secsub = Secsub.objects.all()
    contact = Contact.objects.all()
    home = Home.objects.all()
    return render(request, 'portfolio.html', {'skills':skills, 'project':project, 'biography':biography, 'secsub':secsub, 'contact':contact, 'home':home})


def message(request):
    if request.method == 'POST':
        message = Message()
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.text = request.POST.get('message')
        message.save()
        return HttpResponseRedirect('/')
