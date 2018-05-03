from django.db import models


class TagAbstractBase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)  

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Cause(TagAbstractBase):
    pass


class Skill(TagAbstractBase):
    pass
