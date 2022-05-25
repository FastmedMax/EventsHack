from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Case(models.Model):
    class Type(models.TextChoices):
        HACKATHON = "Hackathon", "Хакатон"
        PRESENTATION = "Presentation", "Презентация"
        WEBSITE = "Website", "Сайт"
        WEBINAR = "Webinar", "Вебинар"
        CORPORATE = "Corporate", "Корпоратив"
        CONFERENCE = "Conference", "Конференция"
        STREAM = "Stream", "Трансляция"
        FREE_FORMAT = "Free_format", "Свободный формат"

    title = models.CharField(verbose_name="Название", max_length=30)
    objective = models.CharField(verbose_name="Цель", max_length=30)
    tasks = models.CharField(verbose_name="Задачи", max_length=100)
    result = models.CharField(verbose_name="Итог", max_length=50)
    banner = models.ImageField(verbose_name="Баннер", blank=True)
    year = models.CharField(verbose_name="Год", max_length=10)
    type = models.CharField(verbose_name="Тип", choices=Type.choices, max_length=30)
    is_best = models.BooleanField(verbose_name="Лучший", default=False)


class Review(models.Model):
    case = models.ForeignKey(
        Case,
        verbose_name="Кейс",
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews"
        )
    photo = models.ImageField(verbose_name="Фото", blank=True)
    name = models.CharField(verbose_name="Имя", max_length=30)
    member_name = models.CharField(verbose_name="Наименование участника", max_length=30, blank=True)
    text = models.TextField(verbose_name="Описание")


class CasePhoto(models.Model):
    case = models.ForeignKey(
        Case,
        verbose_name="Кейс",
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos"
        )
    photo = models.ImageField(verbose_name="Фото")
    caption = models.CharField(verbose_name="Подпись", max_length=30)

    @property
    def photo_url(self):
        return self.photo.url


class Event(models.Model):
    class Type(models.TextChoices):
        HACKATHON = "Hackathon", "Хакатон"
        PRESENTATION = "Presentation", "Презентация"
        WEBSITE = "Website", "Сайт"
        WEBINAR = "Webinar", "Вебинар"
        CORPORATE = "Corporate", "Корпоратив"
        CONFERENCE = "Conference", "Конференция"
        STREAM = "Stream", "Трансляция"
        FREE_FORMAT = "Free_format", "Свободный формат"

    title = models.CharField(verbose_name="Название", choices=Type.choices, max_length=30)
    description = models.TextField(verbose_name="Описание события")
    questions = ArrayField(
        models.TextField(verbose_name="Вопросы")
    )


class Callback(models.Model):
    name = models.CharField(verbose_name="Имя ", max_length=30)
    email = models.EmailField(verbose_name="Почта")
    phone = models.CharField(verbose_name="Номер телефона", max_length=30)
    question = models.CharField(verbose_name="Вопрос", max_length=30)
