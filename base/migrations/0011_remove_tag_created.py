# Generated by Django 4.0.3 on 2022-04-15 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_project_deploylink_alter_project_github'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='created',
        ),
    ]
