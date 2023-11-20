from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Project
from .forms import ProjectForm
# Create your views here.










def projects(request):
    projects = Project.objects.all()
    context = {
        
        "projects": projects
    }
    return render(request, "practiceapp/projects.html", context)

def project(request, pk):
    projectobj = Project.objects.get(id = pk)
    

   
    return render(request, "practiceapp/single-project.html", {
        "project": projectobj,
        
    })
@login_required(login_url="login")
def createproject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")



    context = {
        "form": form
    }
    return render(request, "practiceapp/project_form.html",context)


@login_required(login_url="login")
def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance = project)

    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")



    context = {
        "form": form
    }
    return render(request, "practiceapp/project_form.html",context)


@login_required(login_url="login")
def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")


    context={
        "object":project

    }
    return render(request, "practiceapp/delete.html", context)