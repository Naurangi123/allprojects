from django.utils import timezone
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from pymysql import IntegrityError 
from .forms import ToDoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'todos/home.html')


def signup(request):
    if request.method=='GET':
        return render(request,'todos/signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodo')
            except IntegrityError as e:
                return render(request,'todos/signup.html',{'form':UserCreationForm(),'error':'This username already taken. Please Choose another username.'})
        else:
            return render(request,'todos/signup.html',{'form':UserCreationForm(),'error':"Password didn't match.Try Again"})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todos/login.html', {'form': AuthenticationForm()})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is None:  
            return render(request, 'todos/login.html', {
                'form': AuthenticationForm(),
                'error': 'Username and password did not match.'
            })
        else:
            login(request, user)
            return redirect('currenttodo')
        
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
    
@login_required
def currenttodo(request):
    todos=Todo.objects.filter(user=request.user,datecompleted__isnull=True)
    
    return render(request,'todos/currenttodo.html',{'todos':todos})


@login_required
def createtodo(request):
    form=ToDoForm()
    if request.method=='POST':
        try:
            form=ToDoForm(request.POST)
            if form.is_valid():
                newtodo=form.save(commit=False)
                newtodo.user=request.user
                newtodo.save()
                return redirect('currenttodo')
        except ValueError:
            return render(request,'todos/createtodo.html',{'form':ToDoForm(),'error':'Wrong Data Passed In. Please Enter Valid Data.'})
    else:
        form=ToDoForm()
    return render(request,'todos/createtodo.html',{'form':ToDoForm()})

@login_required
def deletetodo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('currenttodo')


@login_required
def view_updatetodo(request,todo_id):
    todo=get_object_or_404(Todo,id=todo_id)
    if request.method=='GET':
        form=ToDoForm(instance=todo)
        return render(request,'todos/view_update.html',{'form':form,'todo':todo})
    else:
        try:
            form=ToDoForm(request.POST,instance=todo)
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request,'todos/view_update.html',{'form':ToDoForm(),'error':'Wrong Data Passed In. Please Enter Valid Data.'})
        
        
@login_required 
def completetodo(request,todo_id):
    todo=get_object_or_404(Todo,id=todo_id,user=request.user)
    if request.method=='POST':
        todo.datecompleted=timezone.now()
        todo.save()
        return redirect('currenttodo')
@login_required
def completedtodos(request):
    todos=Todo.objects.filter(user=request.user,datecompleted__isnull=False).order_by('-datecompleted')
    
    return render(request,'todos/completed.html',{'todos':todos})