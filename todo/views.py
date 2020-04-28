from django.shortcuts import render, redirect
from .models import Todo
from .forms import AddForm

# Create your views here.
def todo_view(request):
   if request.method == 'POST': # Request == POST?
      form = AddForm(request.POST) # 빈칸에 넣는 정보를 form 에 넣는다.
      if form.is_valid(): # Form의 형식이 유효한지 확인
         form.save() # Form 저장 후 DB에 추가
    
    
   todos = Todo.objects.all()
   form = AddForm()
   data = {
      "todos" : todos,
      "form" : form,
   }
   return render(request, "todo_list.html", data)

def todo_view_progress(request):
    todos = Todo.objects.all()
    data = {
       "todos": todos,
    }
    return render(request, "todo_list_yet.html", data)

def delete_todo(request, pk):
   target = Todo.objects.get(pk=pk)
   target.delete() # 해당 튜플을 제거
   return redirect("todos") # name=“todos” 주소로 돌아감
