from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import modelform_factory

from .models import Task


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/detail.html'

    def get_queryset(self):
        return self.model.objects.select_related('user', 'cause', 'skill')


class TaskCreateView(LoginRequiredMixin, View):
    model = Task
    template_name = 'tasks/create.html'

    def get_form_class(self):
        return modelform_factory(self.model, fields=['cause', 'skill', 'name', 'description'])

    def get(self, request):
        form = self.get_form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect(task.get_absolute_url())
        return render(request, self.template_name, {'form': form}, status=400)


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, SingleObjectMixin, View):
    raise_exception = True
    model = Task

    def test_func(self):
        return self.get_object().user == self.request.user

    def post(self, request, pk):
        return HttpResponse('hi')


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/list.html'

    def get_queryset(self):
        return self.model.objects.select_related('user', 'cause', 'skill')
