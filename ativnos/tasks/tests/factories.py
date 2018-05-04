import factory

from ativnos.users.tests.factories import UserFactory
from ativnos.tags.tests.factories import CauseFactory, SkillFactory

from ativnos.tasks import models


class TaskFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    cause = factory.SubFactory(CauseFactory)
    skill = factory.SubFactory(SkillFactory)

    name = factory.Sequence(lambda n: f"name-{n}")
    description = factory.Sequence(lambda n: f"description-{n}")

    class Meta:
        model = models.Task
