# Generated by Django 3.0.4 on 2020-03-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0011_auto_20200307_1533'),
    ]

    operations = [
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
