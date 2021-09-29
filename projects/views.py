from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ProjectForm
from django.db.models import Q
from .models import Project, Tag
from .utils import projectSearch


def projects(request):
    projects, search_query = projectSearch(request)

    page = request.GET.get('page')
    results = 2
    paginator = Paginator(projects, results)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1


    rightIndex = (int(page) + 1)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages 


    customRange = range(leftIndex, rightIndex+1)

    try:
        projects = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except:
        page = paginator.num_pages
        projects = paginator.page(page)



    context = {'projects':projects, 'search_query':search_query, 'paginator':paginator, 'customRange':customRange}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    context = {'projectObj':projectObj}
    return render(request, 'projects/single-project.html', context)

# View to create the project
@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

# View to update the project
@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


# View to delete the project
@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object':project}
    return render(request, 'delete_template.html', context)
    