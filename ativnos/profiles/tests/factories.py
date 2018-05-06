import factory

from ativnos.profiles import models
from ativnos.tags.tests.factories import CauseFactory, SkillFactory
from ativnos.users.tests.factories import UserFactory


class AbstractUserTagFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)


class UserCauseFactory(AbstractUserTagFactory):
    tag = factory.SubFactory(CauseFactory)

    class Meta:
        model = models.UserCause


class UserSkillFactory(AbstractUserTagFactory):
    tag = factory.SubFactory(SkillFactory)

    class Meta:
        model = models.UserSkill
