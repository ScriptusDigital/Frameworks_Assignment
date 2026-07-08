from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm
from .models import Project

# Logic for handling project-related views and actions
# List View

# Control for user role to view all projects
def user_can_view_all_projects(user):

    if user.has_perm("projects.can_view_all_projects"):
        return True
    
    if hasattr(user, "profile") and user.profile.role in ["manager", "admin"]:
        return True
    
    return False

#List view
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        if user_can_view_all_projects(self.request.user):
            return Project.objects.all()
        
        return Project.objects.filter(owner=self.request.user)

# Detail View

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        if user_can_view_all_projects(self.request.user):
            return Project.objects.all()
        
        return Project.objects.filter(owner=self.request.user)

# Create View

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    success_url = '/projects/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Project created successfully.')
        return super().form_valid(form)

# Update View

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    success_url = '/projects/'

    def get_queryset(self):
        if user_can_view_all_projects(self.request.user):
            return Project.objects.all()
        
        return Project.objects.filter(owner=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully.')
        return super().form_valid(form)

# Delete View

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = '/projects/'

    def get_queryset(self):
        if self.request.user.has_perm('projects.can_view_all_projects'):
            return Project.objects.all()
        
        return Project.objects.filter(owner=self.request.user)
    

    def form_valid(self, form):
        messages.success(self.request, 'Project deleted successfully.')
        return super().form_valid(form)
    

