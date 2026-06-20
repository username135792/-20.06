from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    birth_date = models.DateField(verbose_name='Дата рождения')
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.fio


class Application(models.Model):
    TRANSPORT_CHOICES = [
        ('boat', 'Катер'),
        ('cruise', 'Круизный лайнер'),
        ('yacht', 'Яхта'),
    ]
    PAYMENT_CHOICES = [
        ('card', 'Банковская карта'),
        ('cash', 'Наличные'),
        ('transfer', 'Безналичный перевод'),
    ]
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('studying', 'Идет обучение'),
        ('completed', 'Обучение завершено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', verbose_name='Пользователь')
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_CHOICES, verbose_name='Вид транспорта')
    start_date = models.DateField(verbose_name='Дата начала обучения')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, verbose_name='Способ оплаты')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_transport_type_display()} — {self.user.username} ({self.get_status_display()})'


class Review(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE, related_name='review', verbose_name='Заявка')
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв на {self.application}'
