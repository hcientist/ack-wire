# Generated by Django 2.1.7 on 2019-03-05 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective', models.DateTimeField(auto_now_add=True)),
                ('state', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.Game')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gamestate',
            unique_together={('game', 'effective')},
        ),
    ]