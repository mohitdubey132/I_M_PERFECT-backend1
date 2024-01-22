# Generated by Django 4.2.5 on 2024-01-21 10:47

from django.db import migrations, models
from django.utils import timezone


def set_default_joining_date(apps, schema_editor):
    CustomUser = apps.get_model('restAPI', 'CustomUser')
    for user in CustomUser.objects.all():
        user.joining_date = timezone.now()
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            name='joining_date',
            field=models.DateTimeField(auto_now_add=True),
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.RunPython(set_default_joining_date),
    ]
