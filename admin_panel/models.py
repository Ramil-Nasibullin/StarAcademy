from django.db import models


# Create your models here.


class Planet(models.Model):
    name = models.CharField(max_length=20, verbose_name='Планета:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'


class Test(models.Model):

    test_list = models.TextField(max_length=1000, verbose_name='Тестовое испытание:')
    answer = models.BooleanField('Поставьте галочку если ответ "ДА"', default=False)

    def __str__(self):
        return 'Тест - {0}, Ответ - {1}'.format(self.test_list, self.answer)

    class Meta:
        verbose_name = 'Тестовое испытание'
        verbose_name_plural = 'Тестовые испытания'


class Sith(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя:')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Название планеты:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'


