from django.contrib import admin
from .models import Profile, Skill

# Checking if github is working fine
# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)

