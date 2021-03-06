# Generated by Django 3.2.6 on 2021-08-13 02:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogger', '0002_alter_dog_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalkerScheduler',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('walker', models.UUIDField()),
                ('day', models.PositiveIntegerField(choices=[('0', 'sunday'), ('1', 'monday'), ('2', 'tuesday'), ('3', 'wednesday'), ('4', 'thursday'), ('5', 'friday'), ('6', 'saturday')], validators=[django.core.validators.MaxValueValidator(6)])),
                ('start', models.PositiveIntegerField()),
                ('end', models.PositiveIntegerField()),
                ('sizes', models.ManyToManyField(related_name='sizes', to='dogger.DogSize')),
            ],
        ),
    ]
