from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email')
    search_fields = ('first_name', 'last_name', 'email')
