# Generated by Django 3.0.6 on 2020-05-06 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                ('day_of_birth', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cast',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('character_name', models.CharField(max_length=255)),
                (
                    'actor',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='cinema.Actor',
                        verbose_name='actor',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                (
                    'casting',
                    models.ManyToManyField(
                        blank=True,
                        through='cinema.Cast',
                        to='cinema.Actor',
                        verbose_name='casting',
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='cinema.Movie',
                verbose_name='movie',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='cast',
            unique_together={('movie', 'actor', 'character_name')},
        ),
    ]
