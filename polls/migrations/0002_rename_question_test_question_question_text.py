# Generated by Django 5.1.4 on 2025-01-13 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_test',
            new_name='question_text',
        ),
    ]
