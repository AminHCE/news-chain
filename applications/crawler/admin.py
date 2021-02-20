from django.contrib import admin

from .models import Agency, News, Config


# Register your models here.
admin.site.register(Agency)
admin.site.register(News)
admin.site.register(Config)
