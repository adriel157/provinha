from django.shortcuts import render,redirect
from django.shortcuts import render
from .models import Aluno
from .forms import AlunoForm


# Create your views here.

def listar(request):
        alunos = Aluno.objects.all()
        return render(request, 'escola/index.html', {'alunos': alunos})

def cadastrar(request):
        if request.method == 'POST':
                form = AlunoForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('index')
        else:
                form = AlunoForm()
        return render(request, 'escola/cadastro_aluno.html', {'form': form})


def editar(request, id):
        aluno = Aluno.objects.get(id=id)
        if request.method == 'POST':
                form = AlunoForm(request.POST, instance=aluno)
                if form.is_valid():
                        form.save()
                        return redirect('index')
        else:
                form = AlunoForm(instance=aluno)
        return render(request, 'escola/cadastro_aluno.html', {'form': form, 'aluno': aluno})


def deletar(request, id):
        aluno = Aluno.objects.get(id=id)
        aluno.delete()
        return redirect('index')
       

 

