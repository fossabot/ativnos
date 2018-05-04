from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin

from ativnos.tags.models import Cause, Skill

from .models import UserCause, UserSkill


class UserProfileView(View):
    model = get_user_model()

    def get_queryset(self):
        return self.model.objects.prefetch_related('skills__tag').prefetch_related('causes__tag')

    def get(self, request, pk):

        user = get_object_or_404(self.get_queryset(), pk=pk)
        return render(request, 'profiles/profile_detail.html', {'user': user})


class UpdateProfileView(View):
    template_name = 'profiles/update.html'
    model = get_user_model()
    
    def get_form_class(self):
        return modelform_factory(self.model, fields=['name', 'description'])

    def get(self, request):
        instance = request.user
        form = self.get_form_class()(instance=instance)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        instance = request.user
        form = self.get_form_class()(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(instance.get_absolute_url())
        return render(request, self.template_name, {'form': form}, status=400)


class AbstractUpsertTagView(LoginRequiredMixin, View):
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
            user_tag = form.save(commit=False)
            user_tag.user = request.user
            user_tag.tag = tag
            user_tag.save()
            return redirect(request.user.get_absolute_url())
        return render(
            request, self.template_name,
            {'tag': tag, 'user_tag': user_tag, 'form': form}, status=400)


class UpsertCause(AbstractUpsertTagView):
    model = UserCause
    tag = Cause


class UpsertSkill(AbstractUpsertTagView):
    model = UserSkill
    tag = Skill


class AbstractDeleteUserTagView(LoginRequiredMixin, View):
    def post(self, request, pk):
        user_tag = get_object_or_404(self.model, tag__pk=pk, user=request.user)
        user_tag.delete()
        return redirect(request.user.get_absolute_url())


class DeleteCause(AbstractDeleteUserTagView):
    model = UserCause


class DeleteSkill(AbstractDeleteUserTagView):
    model = UserSkill
