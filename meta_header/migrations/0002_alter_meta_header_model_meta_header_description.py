# Generated by Django 4.1.3 on 2022-11-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_header', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta_header_model',
            name='meta_header_description',
            field=models.TextField(),
        ),
    ]
