# Generated by Django 4.1.3 on 2022-11-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0002_alter_header_model_my_image_alt_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='header_model',
            name='my_skills',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
