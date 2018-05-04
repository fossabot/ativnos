import factory

from ativnos.tags import models


class AbstractTagFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: f"tag-{n}")


class CauseFactory(AbstractTagFactory):
    class Meta:
        model = models.Cause


class SkillFactory(AbstractTagFactory):
    class Meta:
        model = models.Skill
