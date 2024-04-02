from django.contrib import admin
from .models import About

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Check if an instance of About already exists
        about_instance = About.objects.exists()
        # Allow adding if no instance exists, deny otherwise
        return not about_instance

admin.site.register(About, AboutAdmin)



