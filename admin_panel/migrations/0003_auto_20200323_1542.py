# Generated by Django 3.0.4 on 2020-03-23 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_auto_20200323_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='planet',
            options={'verbose_name': 'Планета', 'verbose_name_plural': 'Планеты'},
        ),
        migrations.AlterModelOptions(
            name='sith',
            options={'verbose_name': 'Ситх', 'verbose_name_plural': 'Ситхи'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Тестовое испытание', 'verbose_name_plural': 'Тестовые испытания'},
        ),
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Планета:'),
        ),
        migrations.AlterField(
            model_name='sith',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя:'),
        ),
        migrations.AlterField(
            model_name='sith',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.Planet', verbose_name='Название планеты:'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_list',
            field=models.TextField(max_length=1000, verbose_name='Тестовое испытание:'),
        ),
    ]
