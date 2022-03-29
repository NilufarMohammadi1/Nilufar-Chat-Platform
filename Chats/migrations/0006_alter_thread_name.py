# Generated by Django 4.0.3 on 2022-03-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chats', '0005_alter_thread_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='name',
            field=models.CharField(choices=[('individual', 'Individual'), ('group', 'Group')], default='New Chat', max_length=20),
        ),
    ]
