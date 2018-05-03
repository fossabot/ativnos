from django.views import View
from django.shortcuts import render


class TaskView(View):
    def get(self, request, pk):
        return render(request, 'tasks/detail.html')