from django.contrib import admin
from . import models


admin.site.register(models.Sith)


class PlanetID(admin.ModelAdmin):
    list_display = [field.name for field in models.Planet._meta.fields]

    class Meta:
        model = models.Planet


class TestID(admin.ModelAdmin):
    list_display = [field.name for field in models.Test._meta.fields]

    class Meta:
        model = models.Test


admin.site.register(models.Planet, PlanetID)
admin.site.register(models.Test, TestID)