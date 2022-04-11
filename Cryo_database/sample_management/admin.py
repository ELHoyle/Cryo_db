from django.contrib import admin
# Register your models here.

from .models import Sample, Location
admin.site.register(Sample)
admin.site.register(Location)
