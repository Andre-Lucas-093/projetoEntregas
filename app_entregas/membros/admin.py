from django.contrib import admin
from .models import Membro

from .models import Membro

# Register your models here.

class MembroAdmin(admin.ModelAdmin):
  list_display = ("nome", "codigo")
  
admin.site.register(Membro, MembroAdmin)

# Register your models here.
