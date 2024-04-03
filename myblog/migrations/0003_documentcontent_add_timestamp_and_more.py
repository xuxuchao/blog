# Generated by Django 4.2 on 2024-04-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_alter_documentcontent_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentcontent',
            name='add_timestamp',
            field=models.DateTimeField(auto_now_add=True, default='2023-10-24 13:06:11.007 +0800', verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documentcontent',
            name='update_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
