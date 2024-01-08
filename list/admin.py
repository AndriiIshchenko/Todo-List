from django.contrib import admin

from list.models import Tag, Task

# Register your models here.
admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "priority")
