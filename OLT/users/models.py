from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name='город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payments(models.Model):
    from materials.models import Course, Lesson

    Cash = 1
    Transfer = 2

    METHOD = [
        (Cash, "Наличные"),
        (Transfer, "Перевод на счет")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_pay = models.DateTimeField(verbose_name='дата оплаты')
    pay_course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=True)
    pay_lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, null=True, blank=True)
    pay_summ = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма оплаты')
    pay_method = models.PositiveSmallIntegerField(default=1, choices=METHOD, verbose_name='Способ оплаты')

    def __str__(self):
        return f"{self.date_pay}, {self.pay_summ}, {self.pay_method}"

    class Meta:
        verbose_name = "Платежи"
