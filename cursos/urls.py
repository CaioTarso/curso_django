from django.urls import path
from . import views

urlpatterns = [
    path('listar_cursos/', views.listar_cursos, name="listar_cursos"),
    path('criar_curso/', views.criar_curso, name="criar_curso"),
    path('ver_curso/<int:id>', views.ver_curso, name="ver_curso"),
    path('deletar_curso/<int:id>', views.deletar_curso, name="deletar_curso")

]
