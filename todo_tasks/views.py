from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import Task
from .forms import CreateUserForm, TaskForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from .decorators import unauthenticated_user

# Create your views here.
class TaskListView(ListView):
   model = Task
   template_name = "base.html"
   context_object_name = "task"

   def get_queryset(self):
      account_list =Task.objects.filter(user=self.request.user)
      return account_list

class TaskCreateView(CreateView):
   model = Task
   form_class = TaskForm 
   template_name = "todo_tasks/task_form.html"
   
   def get_success_url(self):
      return reverse('intro')

   def form_valid(self, form):
      form.instance.user = self.request.user
      return super(TaskCreateView, self).form_valid(form)

@login_required(login_url='login')
def thank_you(request):
   return render(request, 'todo_tasks/success.html')

class TaskDeleteView(DeleteView):
   model = Task
   context_object_name= 'tasks'
   success_url= reverse_lazy('intro')

class TaskUpdateView(UpdateView):
   model = Task
   context_object_name= 'tasks'
   fields= ['task', 'details', 'date']
   success_url= reverse_lazy('intro')

@unauthenticated_user
def registerUser(request):
   form= CreateUserForm()

   if request.method=='POST':
      form= CreateUserForm(request.POST)
      if form.is_valid:
         form.save()
         user=form.cleaned_data.get('username')
         messages.success(request, 'Account was created for'+user)
         return redirect('login')

      
   context={'form':form}
   return render(request, 'todo_tasks/register.html', context)

class LoginUser(LoginView):
   template_name= 'todo_tasks/login.html'
   fields= '__all__'
   redirect_authenticated_user= True

   def get_success_url(self):
      return reverse_lazy('intro')


class RegisterUser(FormView):
   template_name= 'todo_tasks/register.html'
   form_class= CreateUserForm
   redirect_authenticated_user = True
   success_url = reverse_lazy('intro')

   def form_valid(self, form):
      user = form.save()
      if user is not None:
         login(self.request, user)
      return super(RegisterUser, self).form_valid(form)

   def get(self, *args, **kwargs):
      if self.request.user.is_authenticated:
         return redirect('intro')
      return super(RegisterUser, self).get(*args, **kwargs)

# @unauthenticated_user
# def loginUser(request):
#    if request.method=='POST':
#       username= request.POST.get('username')
#       password= request.POST.get('password')

#       user= authenticate(request, username=username, password= password)

#       if user is not None:
#          login(request, user)
#          return redirect('intro')
#       else:
#          messages.info(request, 'Username or password is incorrect.')

#    context={}
#    return render(request, 'todo_tasks/login.html', context)

def logoutUser(request):
   logout(request)
   return redirect('login')