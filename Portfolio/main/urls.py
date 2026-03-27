from django.urls import path
from django_distill import distill_path
from django.apps import apps

from . import views


def get_project_ids():
    project_model = apps.get_model('main', 'Project')
    return ((project_id,) for project_id in project_model.objects.values_list('id', flat=True))

urlpatterns = [
    distill_path('', views.home, name='home'),
    path('home/', views.home, name='home_alias'),
    distill_path('projects/', views.projects, name='projects'),
    distill_path('contact/', views.contact, name='contact'),
    distill_path('project/<int:id>/', views.project, name='project', distill_func=get_project_ids),
]