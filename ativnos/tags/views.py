from django.views.generic.list import ListView

from .models import Cause, Skill


class AbstractTagListView(ListView):
    template_name = 'tags/tag_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = "{0}s".format(self.model.__name__)
        return context


class CauseListView(AbstractTagListView):
    model = Cause


class SkillsListView(AbstractTagListView):
    model = Skill
