from django.contrib import admin

from .models import UserCause, UserSkill


@admin.register(UserCause)
class UserCauseAdmin(admin.ModelAdmin):
    pass


@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    pass
