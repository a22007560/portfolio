
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home_page_view, name='home'),
    path("licenciatura", views.licenciatura_page_view, name='licenciatura'),
    path("projetos", views.projetos_page_view, name='projetos'),
    path("blog", views.blog_page_view, name='blog'),
    path('newPost/', views.nova_blog_view, name='newPost'),
    path('editPost/<int:blog_id>', views.edita_blog_view, name='editPost'),
    path('deletePost/<int:blog_id>', views.apaga_blog_view, name='deletePost'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('login', views.login_page_view, name='login'),
    path('weather', views.weather_page_view, name='weather'),

]