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
