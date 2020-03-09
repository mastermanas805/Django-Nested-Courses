# Generated by Django 3.0.3 on 2020-03-09 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0016_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_topics',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='sub_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='create.sub_topics'),
        ),
    ]
