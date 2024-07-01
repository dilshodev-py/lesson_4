from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, DeleteView

from apps.forms import TaskForm
from apps.models import Task


class TaskListView(ListView):
    queryset = Task.objects.filter()
    context_object_name = 'tasks'
    template_name = 'apps/task-list.html'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'apps/task-detail.html'

class TaskFormView(FormView):
    form_class = TaskForm
    success_url = 'task-list'
    template_name = 'apps/task-form.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request , 'apps/task-form.html', {'form': form})
        return redirect('task-list')


class TaskDeleteView(View):
    def get(self , request ,pk):
        Task.objects.filter(pk = pk).first().delete()
        return redirect('task-list')


git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/dilshodev3234/lesson_4.git
git push -u origin main




