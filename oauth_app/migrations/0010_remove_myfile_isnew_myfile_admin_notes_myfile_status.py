# Generated by Django 4.2.10 on 2024-03-31 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_app', '0009_myfile_isnew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myfile',
            name='isNew',
        ),
        migrations.AddField(
            model_name='myfile',
            name='admin_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='myfile',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='new', max_length=20),
        ),
    ]
