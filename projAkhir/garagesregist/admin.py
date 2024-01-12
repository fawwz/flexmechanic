from django.contrib import admin
from .models import Garage
from account.models import Mechanic


# Register your models here.
@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
  model = Garage
  list_display = ('garage_id','get_garage_owner','garage_name', 'address')
  search_fields = ('garage_id','garage_name')
  ordering = ('garage_id',)
  
  def get_garage_owner(self, obj):
        mechanic = Mechanic.objects.get(garage=obj)
        return mechanic.user_profile.email

