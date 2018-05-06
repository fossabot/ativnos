from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import DeleteView, DetailView, ListView

from ativnos.helpers.views import CreateView

from .models import Task


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_queryset(self):
        return self.model.objects.select_related('user', 'cause', 'skill')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/create.html'
    fields = ['cause', 'skill', 'name', 'description']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class TaskDeleteView(UserPassesTestMixin, DeleteView):
    http_method_names = ['post']
    raise_exception = True
    model = Task

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return f'{self.request.user.get_absolute_url()}#tasks'


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'

    def get_queryset(self):
        return self.model.objects.select_related('user', 'cause', 'skill')
