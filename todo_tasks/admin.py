from django.contrib import admin
from .models import Task
# Register your models here.

admin.site.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display=('task')
    actions= None

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()
    

