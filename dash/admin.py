from django.contrib import admin
from .models import Dash # add this

# Register your models here.


class DashAdmin(admin.ModelAdmin):  # add this
  list_display = ('label', 'value') # add this

# Register your models here.
admin.site.register(Dash, DashAdmin) # add this