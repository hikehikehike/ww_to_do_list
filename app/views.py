from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from app.forms import TaskForm
from app.models import Task


class TaskListViews(generic.ListView):
    model = Task
    fields = "__all__"


class TaskDetailViews(generic.DetailView):
    model = Task
    fields = "__all__"


class TaskCreationViews(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskUpdateViews(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskDeleteViews(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:task-list")


def complete_undo(request, pk):
    task = Task.objects.get(pk=pk)
    task.done_or_not = not task.done_or_not
    task.save()
    return HttpResponseRedirect(reverse_lazy("todolist:task-list"))
