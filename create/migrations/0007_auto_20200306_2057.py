# Generated by Django 3.0.3 on 2020-03-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0006_auto_20200302_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_topics',
            name='contect',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='sub_topics',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='sub_topics',
            name='pdf',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
