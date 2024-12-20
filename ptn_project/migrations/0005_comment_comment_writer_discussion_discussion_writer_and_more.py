# Generated by Django 5.1.2 on 2024-11-11 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_name'),
        ('ptn_project', '0004_alter_discussionimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='accounts.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discussion',
            name='discussion_writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='discussion', to='accounts.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incomment',
            name='in_comment_writer',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='in_comment', to='accounts.account'),
            preserve_default=False,
        ),
    ]
