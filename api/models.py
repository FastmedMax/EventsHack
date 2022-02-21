from django.db import models

# Create your models here.
class Case(models.Model):
    class Type(models.Choices):
        Hackathon = "Hackathon"
        PRESENTATION = "Presentation"
        WEBSITE = "Website"
        WEBINAR = "Webinar"
        CORPORATE = "Corporate"
        CONFERENCE = "Conference"
        STREAM = "Stream"
        FREE_FORMAT = "Free_format"

    title = models.CharField(verbose_name="Название", max_length=30)
    objective = models.CharField(verbose_name="Цель", max_length=30)
    tasks = models.CharField(verbose_name="Задачи", max_length=100)
    result = models.CharField(verbose_name="Итог", max_length=50)
    banner = models.ImageField(verbose_name="Баннер")
    year = models.CharField(verbose_name="Год", max_length=10)
    type = models.CharField(verbose_name="Тип", choices=Type.choices)


class Review(models.Model):
    case = models.ForeignKey(
        Case,
        verbose_name="Кейс",
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews"
        )
    photo = models.ImageField(verbose_name="Фото")
    name = models.CharField(verbose_name="Имя рецензиста", max_length=30)
    member_name = models.CharField(verbose_name="Роль", max_length=30)
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


class Callback(models.Model):
    name = models.CharField(verbose_name="Имя ", max_length=30)
    email = models.EmailField(verbose_name="Почта")
    phone = models.CharField(verbose_name="Номер телефона", max_length=30)
    question = models.CharField(verbose_name="Вопрос", max_length=30)
