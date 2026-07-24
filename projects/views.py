from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm
from .models import Project

# Logic for handling project-related views and actions
# List View

# Control for user role to view all projects
def user_can_view_all_projects(user):
    """Return whether a user may access projects belonging to all users."""
    if user.has_perm("lass ProjectListView(LoginRequiredMixin, ListView):projects.can_view_all_projects"):
        return True
    
    if hasattr(user, "profile") and user.profile.role in ["manager", "admin"]:
        return True
    
    return False

#List view
class ProjectListView(LoginRequiredMixin, ListView):
    """List projects available to the logged-in user."""
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        """Return projects in display"""
        if user_can_view_all_projects(self.request.user):
            return Project.objects.all()
        
        return Project.objects.filter(owner=self.request.user)
    
    def get_context_data(self):
        """Return projects in display when role is higher permission level"""
        context = super().get_context_data()
        context["can_view_all_projects"] = user_can_view_all_projects(self.request.user)
        return context
    
# Detail View

class ProjectDetailView(LoginRequiredMixin, DetailView):
    """Display a project when the logged-in user is authorized to access it."""
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_queryset(self):
        if user_can_view_all_projects(self.request.user):
            return Project.objects.all()
        
        return Project.objects.filter(owner=self.request.user)

# Create View

class ProjectCreateView(LoginRequiredMixin, CreateView):
    """Create a project owned by the logged-in user."""
    model = Project
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    success_url = '/projects/'

    def form_valid(self, form):
        """Project creation success message"""
        form.instance.owner = self.request.user
        messages.success(self.request, 'Project created successfully.')
        return super().form_valid(form)

# Update View

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """Update a project when authorized."""
    model = Project
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    success_url = '/projects/'

    def get_queryset(self):
        if user_can_view_all_projects(self.request.user):
            return Project.objects.all()
        
        return Project.objects.filter(owner=self.request.user)
    
    def form_valid(self, form):
        """Save a valid update and display a success message."""
        messages.success(self.request, 'Project updated successfully.')
        return super().form_valid(form)

# Delete View

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    """Confirmm and delete a project when the logged-in user is authorized."""
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = '/projects/'

    def get_queryset(self):
        """Return all projects for elevated roles, otherwise only owned projects."""
        if user_can_view_all_projects(self.request.user):
            return Project.objects.all()
        
        return Project.objects.filter(owner=self.request.user)
    

    def form_valid(self, form):
        """Deletion of project success message."""
        messages.success(self.request, 'Project deleted successfully.')
        return super().form_valid(form)
    

