
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home_page_view, name='home'),
    path("licenciatura", views.licenciatura_page_view, name='licenciatura'),
    path("projetos", views.projetos_page_view, name='projetos'),
    path("newProject/", views.newProject_page_view, name='newProject'),
    path('editProject/<int:project_id>', views.edita_project_view, name='editProject'),
    path('deleteProject/<int:project_id>', views.apaga_project_view, name='deleteProject'),
    path("blog", views.blog_page_view, name='blog'),
    path('newPost', views.nova_blog_view, name='newPost'),
    path('editPost/<int:blog_id>', views.edita_blog_view, name='editPost'),
    path('deletePost/<int:blog_id>', views.apaga_blog_view, name='deletePost'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('weather', views.weather_page_view, name='weather'),
    path('factos', views.factos_page_view, name='factos'),

]