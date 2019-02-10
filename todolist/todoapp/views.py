from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def index(request):
    # return HttpResponse('Hello')
    todo = Todo.objects.all()
    cont = {
        'todo':todo
    }
    return render(request,'index.html',cont)

def details(request,id):
    todo = Todo.objects.get(id = id)
    cont = {
        'todo':todo
    }
    return render(request,'details.html',cont)


def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title,text=text)
        todo.save()
        return redirect('/todoapp')
    else:
        return render(request,'add.html')