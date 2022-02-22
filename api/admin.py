from django.contrib import admin

from .models import CasePhoto, Case, Callback, Event, Review

# Register your models here.
admin.site.register(CasePhoto)
admin.site.register(Case)
admin.site.register(Callback)
admin.site.register(Event)
admin.site.register(Review)