from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name = 'homepage'),
    path('3D_Models', views.ProjectPage, name = 'project_page'),
    path('3D_Models/details/<int:pk>', views.ProjectDetails, name = 'project_details'),
    path('about', views.AboutPage, name = 'about_page'),
    path('create_post', views.CreatePost, name = 'create_post'),
]