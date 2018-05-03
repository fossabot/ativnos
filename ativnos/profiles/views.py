from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin

from ativnos.tags.models import Cause, Skill

from .models import UserCause, UserSkill


class ProfileDetailView(View):
    def get(self, request):
        return render(request, 'profiles/profile_detail.html')


class UpsertTagViewAbstractBase(LoginRequiredMixin, View):
    template_name = 'profiles/upsert_tag.html'

    def get_form_class(self):
        return modelform_factory(self.model, fields=['description'])

    def get(self, request, pk):
        tag = get_object_or_404(self.tag, pk=pk)
        user_tag = self.model.objects.filter(user=request.user, tag=tag).first()
        form = self.get_form_class()(instance=user_tag)
        return render(
            request, self.template_name,
            {'tag': tag, 'user_tag': user_tag, 'form': form})
    
    def post(self, request, pk):
        tag = get_object_or_404(self.tag, pk=pk)
        user_tag = self.model.objects.filter(user=request.user, tag=tag).first()
        form = self.get_form_class()(request.POST, instance=user_tag)
        if form.is_valid():
            return redirect(request.user.get_absolute_url())
        return render(
            request, self.template_name,
            {'tag': tag, 'user_tag': user_tag, 'form': form}, status=400)


class UpsertCause(UpsertTagViewAbstractBase):
    model = UserCause
    tag = Cause


class UpsertSkill(UpsertTagViewAbstractBase):
    model = UserSkill
    tag = Skill


class DeleteUserTagAbstractBase(LoginRequiredMixin, View):
    def post(self, request, pk):
        user_tag = get_object_or_404(self.model, tag__pk=pk, user=request.user)
        user_tag.delete()
        return redirect(request.user.get_absolute_url())


class DeleteCause(DeleteUserTagAbstractBase):
    model = UserCause


class DeleteSkill(DeleteUserTagAbstractBase):
    model = UserSkill
