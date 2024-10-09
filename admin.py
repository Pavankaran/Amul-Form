from django.contrib import admin
from .models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'date', 'category', 'executive_name', 'start_date', 'end_date', 'entry_name')
    search_fields = ('sr_no', 'category', 'executive_name')
    list_filter = ('category', 'executive_name')
