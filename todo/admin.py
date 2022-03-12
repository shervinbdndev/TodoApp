from django.contrib import admin
from .models import TodoDatabase


class TodoDatabaseModelAdmin(admin.ModelAdmin):
    list_display = ['title' , 'created_at' , 'modified_at']


admin.site.register(TodoDatabase , TodoDatabaseModelAdmin)