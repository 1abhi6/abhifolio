# Generated by Django 4.1.3 on 2022-11-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_model',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
