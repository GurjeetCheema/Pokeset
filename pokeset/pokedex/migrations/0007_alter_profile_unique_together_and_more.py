# Generated by Django 4.1 on 2022-09-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0006_alter_ability_name_alter_location_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='profile',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_profiles'),
        ),
    ]