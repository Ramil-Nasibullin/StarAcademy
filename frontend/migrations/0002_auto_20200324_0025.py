# Generated by Django 3.0.4 on 2020-03-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recrutregistrationform',
            name='age',
            field=models.IntegerField(verbose_name='Ваш возраст:'),
        ),
    ]
