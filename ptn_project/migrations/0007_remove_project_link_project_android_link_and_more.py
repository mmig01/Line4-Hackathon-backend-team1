# Generated by Django 5.1.2 on 2024-11-11 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptn_project', '0006_comment_upload_date_discussion_upload_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.AddField(
            model_name='project',
            name='android_link',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='ios_link',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='web_link',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='incomment',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_comment', to='ptn_project.comment'),
        ),
    ]
