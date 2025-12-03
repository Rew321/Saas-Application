from django.shortcuts import render, redirect
from tasks.models import Project
from tasks.forms import ProjectForm
# Create your views here.


def project_list(request):
    print(request.tenant)#added by the Tenants middleware

    projects = Project.objects.all().prefetch_related('tasks')
    context = {
        'projects': projects}

    return render(request, 'tasks/project_list.html', context)


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
        context = {'form': form}
    return render(request, 'tasks/create_project.html', context)