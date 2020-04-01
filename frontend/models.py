from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class RecrutRegistrationForm(models.Model):
    name = models.CharField(max_length=25, verbose_name='Ваше имя:', )
    planet = models.CharField(max_length=50, verbose_name='Ваша планета обитания:')
    age = models.IntegerField(verbose_name='Ваш возраст:')
    mail = models.EmailField(verbose_name='Ваша почта:')

    def __str__(self):
        return 'Имя: %s' % self.name

    class Meta:
        verbose_name = 'Зарегистрированный рекрут'
        verbose_name_plural = 'Зарегистрированные рекруты'

