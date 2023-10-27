from django.contrib import admin
from .models import student

# Register your models here.

@admin.register(student)
class student_admin(admin.ModelAdmin):
  list_display = ('name', 'email')