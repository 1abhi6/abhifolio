# Generated by Django 4.1.3 on 2022-11-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='meta_header_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_header_title', models.CharField(max_length=50)),
                ('meta_header_keyword', models.CharField(max_length=100)),
                ('meta_header_description', models.CharField(max_length=500)),
                ('meta_header_favicon', models.ImageField(default=None, max_length=500, null=True, upload_to='meta_header_favicon')),
            ],
        ),
    ]
