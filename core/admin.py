from django.contrib import admin
from .models import *

class RecordAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'first_name', 'last_name', 'address', 'email', 'phone']

admin.site.register(Record)
