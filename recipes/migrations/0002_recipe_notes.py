# Generated by Django 3.0.5 on 2020-05-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='notes',
            field=models.TextField(default='Recipe notes...'),
        ),
    ]