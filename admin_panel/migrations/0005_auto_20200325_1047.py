# Generated by Django 3.0.4 on 2020-03-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_test_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='answer',
            field=models.BooleanField(default=False, verbose_name='Поставьте галочку если ответ "ДА"'),
        ),
    ]
