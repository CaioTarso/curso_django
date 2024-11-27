from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime


# Create your views here.
def listar_cursos(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    carga_horaria_filtrar = request.GET.get('carga_horaria')


    cursos = Curso.objects.all()

    if nome_filtrar:
        cursos = cursos.filter(nome__contains=nome_filtrar)
    
    # gte retorna os dados iguais ou maiores que o digitado
    if carga_horaria_filtrar:
        cursos = cursos.filter(carga_horaria__gte=carga_horaria_filtrar)

    
    return render(request, 'listar_cursos.html', {'cursos': cursos})


def criar_curso(request):
    if request.method == "GET":
       status = request.GET.get('status')
       

       return render(request, 'criar_curso.html', {'status': status})
    elif request.method == "POST":
        nome_digitado = request.POST.get('nome')
        carga_horaria_digitada = request.POST.get('carga_horaria')

        curso = Curso(
            nome=nome_digitado,
            carga_horaria=carga_horaria_digitada,
            data_criacao=datetime.now()
        )

        curso.save()

        return redirect('/curso/criar_curso/?status=1')

   
def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'ver_curso.html', {'curso': curso})

def deletar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.ativo = False
    curso.save()
    return redirect('/curso/listar_cursos')


