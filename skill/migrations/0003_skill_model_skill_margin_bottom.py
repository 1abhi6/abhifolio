# Generated by Django 4.1.3 on 2022-11-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_skill_model_skill_progress_bar_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill_model',
            name='skill_margin_bottom',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
