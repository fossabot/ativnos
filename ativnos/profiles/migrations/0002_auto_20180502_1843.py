# Generated by Django 2.0.5 on 2018-05-02 18:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercause',
            unique_together={('user', 'tag')},
        ),
        migrations.AlterUniqueTogether(
            name='userskill',
            unique_together={('user', 'tag')},
        ),
    ]
