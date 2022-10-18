from django.contrib import admin

from .models import Bezeroa, Kotxea, KotxeaSortzekoModeloa

# Register your models here.
admin.site.register(Bezeroa)
admin.site.register(Kotxea)
admin.site.register(KotxeaSortzekoModeloa)