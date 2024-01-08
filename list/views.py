from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View, generic

from list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task_list.html"
    ordering = ["is_completed", "-start_time"]
    paginate_by = 2


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:task-list")


class TaskCompletedView(View):
    model = Task

    def post(self, request, **kwargs) -> HttpResponse:
        task = Task.objects.get(id=kwargs["pk"])
        task.is_completed = not task.is_completed
        task.save()
        return redirect("list:task-list")



class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")
