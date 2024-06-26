# Generated by Django 4.2.10 on 2024-03-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth_app', '0002_delete_upload_remove_myfile_title_myfile_uploaded_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myfile',
            name='description',
            field=models.TextField(default='description'),
        ),
        migrations.AddField(
            model_name='myfile',
            name='title',
            field=models.CharField(default=42, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
