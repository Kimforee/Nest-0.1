# Generated by Django 4.2 on 2023-08-22 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearnNest', '0002_topic_nest_host_message_nest_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='room',
            new_name='nest',
        ),
    ]
