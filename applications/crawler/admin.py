from django.contrib import admin

from .models import Agency, News, Config


# Register your models here.
admin.site.register(Agency)


@admin.register(News)
class ProjectAdmin(admin.ModelAdmin):
    save_as = True
    readonly_fields = ['token']


admin.site.register(Config)
