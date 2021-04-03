from django.db import models


class FeedBack(models.Model):
    name = models.CharField('ФИО', max_length=120)
    email = models.EmailField('E-mail', max_length=120, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=15)
    description = models.CharField('Описание', max_length=500, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Форма обратной связи'
