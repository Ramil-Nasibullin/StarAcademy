# Generated by Django 3.0.4 on 2020-03-23 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sith',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.Planet'),
        ),
    ]