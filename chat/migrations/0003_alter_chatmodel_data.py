# Generated by Django 4.1 on 2022-08-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]