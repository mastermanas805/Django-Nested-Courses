# Generated by Django 3.0.3 on 2020-03-06 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0007_auto_20200306_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub_topics',
            old_name='contect',
            new_name='content',
        ),
    ]