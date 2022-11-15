# Generated by Django 4.1.3 on 2022-11-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_model_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_model',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact_model',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact_model',
            name='subject',
            field=models.TextField(null=True),
        ),
    ]
