from django.shortcuts import redirect, render
from .models import Project
from django.core.paginator import Paginator
from .forms import ProjectForm
# Create your views here.

def Homepage(request):
    project = Project.objects.all()
    context = {'project': project[0]}
    return render(request, 'index.html', context)

def ProjectPage(request):
    projects = Project.objects.all()
    projects_pan = Paginator(projects, 2)
    page = request.GET.get('page')
    projects = projects_pan.get_page(page)
    context = {'projects':projects}
    return render(request, 'project.html', context)

def ProjectDetails(request, pk):
    project = Project.objects.get(id = pk)
    context = {'project':project}
    return render(request, 'project_details.html', context)


def AboutPage(request):
    context = {}
    return render(request, 'about.html', context)

def CreatePost(request):
    form = ProjectForm()
    context = {'form':form}
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        cover_image = request.FILES['cover_image']
        other_image1 = request.FILES['other_image1']
        if form.is_valid:
            form = Project.objects.create(name = name, description=description, cover_image = cover_image, other_image1 = other_image1)
            form.save()
            return redirect('homepage')
        else:
            print('not working')
    else:
        return render(request, 'create_post.html', context)
    return render(request, 'create_post.html', context)