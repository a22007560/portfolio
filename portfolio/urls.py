
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home_page_view, name='home'),
    path("licenciatura", views.licenciatura_page_view, name='licenciatura'),
    path('novaCadeira', views.novaCadeira_page_view, name='novaCadeira'),
    path('editCadeira/<int:cadeira_id>', views.edita_cadeira_view, name='editCadeira'),
    path('deleteCadeira/<int:cadeira_id>', views.apaga_cadeira_view, name='deleteCadeira'),
    path("projetos", views.projetos_page_view, name='projetos'),
    path("newProject/", views.newProject_page_view, name='newProject'),
    path('editProject/<int:project_id>', views.edita_project_view, name='editProject'),
    path('deleteProject/<int:project_id>', views.apaga_project_view, name='deleteProject'),
    path("newTFC/", views.newTFC_page_view, name='newTFC'),
    path("blog", views.blog_page_view, name='blog'),
    path('newPost', views.nova_blog_view, name='newPost'),
    path('editTFC/<int:tfc_id>', views.edita_tfc_view, name='editTFC'),
    path('deleteTFC/<int:tfc_id>', views.apaga_tfc_view, name='deleteTFC'),
    path('editPost/<int:blog_id>', views.edita_blog_view, name='editPost'),
    path('deletePost/<int:blog_id>', views.apaga_blog_view, name='deletePost'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('weather', views.weather_page_view, name='weather'),
    path('factos', views.factos_page_view, name='factos'),
    path('noticias', views.noticias_page_view, name='noticias'),

]