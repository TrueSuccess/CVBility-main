# Generated by Django 4.1.4 on 2022-12-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0003_resumetemplates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumetemplates',
            name='page',
            field=models.TextField(default=True, null=True),
        ),
    ]
