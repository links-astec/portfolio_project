from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Project

#this is for the normal pages
def home(request):
    return render(request, "personal_portfolio/home.html", {})


def portfolio(request):
    return render(request,"personal_portfolio/portfolio_list.html",{})

def skills(request):
    return render(request,"personal_portfolio/skills.html",{})

def experience(request):
    return render(request,"personal_portfolio/experience.html",{})


def contact(request):
    return render(request, "personal_portfolio/contacts.html",{})



#project views
class ProjectList(ListView):
    model= Project
    template_name = 'personal_portfolio/project.html'
    context_object_name = 'project_data'
    paginate_by = 2



def project_create(request):
    new_project = Project()

    if request.method == 'POST':
        new_project.title = request.POST.get('title', '')
        new_project.description = request.POST.get('description', '')
        new_project.credential = request.POST.get('credential', '')       
        new_project.save()
        return redirect('project')

    return render(request, 'personal_portfolio/add_project.html', context={'project': new_project})



def project_update(request, project_index):
    project_to_update = Project.objects.get(pk=project_index)

    if request.method == 'POST':
        project_to_update.title = request.POST['title']
        project_to_update.credential = request.POST['credential']
        project_to_update.description=request.POST['description']       
        project_to_update.save()
        return redirect('project')
    return render(request, 'personal_portfolio/update_project.html',context={'project':project_to_update})



def project_delete(request, project_index):
    project_to_delete = Project.objects.get(pk=project_index)
    if request.method == 'POST':
        project_to_delete.delete()
        return redirect('project')
    return render(request, 'personal_portfolio/delete_project.html', context={'project': project_to_delete})

