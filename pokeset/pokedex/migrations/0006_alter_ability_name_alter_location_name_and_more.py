# Generated by Django 4.1 on 2022-09-17 11:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pokedex', '0005_capable_pokemon_abilities_alter_ability_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='move',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='ability',
            unique_together={('name', 'profile')},
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('name', 'profile')},
        ),
        migrations.AlterUniqueTogether(
            name='move',
            unique_together={('name', 'profile')},
        ),
        migrations.AlterUniqueTogether(
            name='pokemon',
            unique_together={('name', 'profile')},
        ),
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together={('name', 'user')},
        ),
    ]