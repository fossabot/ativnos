from django.views import View
from django.shortcuts import render


class ProfileDetailView(View):
    def get(self, request):
        return render(request, 'profiles/profile_detail.html')
