# Generated by Django 2.2.10 on 2020-04-13 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20200407_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='double_tiles_variant',
            field=models.BooleanField(default=False),
        ),
    ]
