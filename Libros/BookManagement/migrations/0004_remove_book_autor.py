# Generated by Django 4.0.2 on 2022-02-16 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookManagement', '0003_autor_editorial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='autor',
        ),
    ]
