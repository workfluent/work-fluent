from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_deleted', 'deleted_at')
    list_filter = ('is_deleted', 'created_at')
    search_fields = ('name', 'email')
