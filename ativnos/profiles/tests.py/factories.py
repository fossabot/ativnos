import factory

from ativnos.users.tests.factories import UserFactory
from ativnos.tags.tests.factories import CauseFactory, SkillFactory

from ativnos.profiles import models


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
