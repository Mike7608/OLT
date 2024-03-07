from django.db import models

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    pict = models.ImageField(upload_to='course/', verbose_name='превью', null=True, blank=True)
    description = models.CharField(max_length=250, verbose_name='описание', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, verbose_name='user_id')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    pict = models.ImageField(upload_to='lesson/', verbose_name='превью', null=True, blank=True)
    url_video = models.URLField(verbose_name='видео ссылка', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, verbose_name='user_id')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

