from django.contrib import admin

from .models import Cause, Skill


@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass
