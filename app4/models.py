from django.db import models

# Create your models here.


class Announcement(models.Model):

    # NICK NAME should be unique
    nick_name = models.CharField(max_length=100, verbose_name='Объявление',  unique =  True)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, verbose_name=' Рубрика', null=True)

    def __str__(self):
        return self.nick_name


class Rubric (models .Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
