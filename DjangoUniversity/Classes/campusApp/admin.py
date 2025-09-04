from django.contrib import admin
# Import the UniversityCampus class from the campusApp models
from .models import UniversityCampus

# Register your models here. This tells the site that when user adds /admin to the url this is where to come for
# the data.
admin.site.register(UniversityCampus)