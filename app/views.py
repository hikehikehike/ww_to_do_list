from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
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


class TaskCreationViews(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateViews(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskDeleteViews(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:task-list")


@login_required
def complete_undo(request, pk):
    task = Task.objects.get(pk=pk)
    task.done_or_not = not task.done_or_not
    task.save()
    next_url = request.GET.get("next")
    if next_url:
        return redirect(next_url)
