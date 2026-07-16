from django.urls import path
from . views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectDeleteView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("project/new/", ProjectCreateView.as_view(), name="project_create"),
    path("project/<int:pk>/update/", ProjectUpdateView.as_view(), name="project_update"),
    path("project/<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),

]