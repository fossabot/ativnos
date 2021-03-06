# Generated by Django 2.0.5 on 2018-05-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(
                blank=True,
                help_text=
                'Describe yourself. What have you done? What do you want to do? Include ways to be contacted if you want to help.',
                max_length=700,
                verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(
                blank=True,
                help_text='Name displayed to other users',
                max_length=255,
                verbose_name='Display Name'),
        ),
    ]
