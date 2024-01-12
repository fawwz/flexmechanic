from django.http import HttpResponse
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.gis import admin as gis_admin
# from import_export import resources
# from import_export.admin import ExportMixin, ImportMixin, ImportExportModelAdmin

from .models import CustomUser, Customer, Mechanic


# class CustomUserResource(resources.ModelResource):
#   class Meta:
#     model = CustomUser
#     fields = ('id', 'email', 'account_type', 'first_name',
#               'last_name', 'is_active', 'is_staff', 'is_verified')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
#   resource_class = CustomUserResource
#   model = CustomUser

  list_display = ('email', 'id', 'account_type', 'first_name',
                  'last_name', 'is_active', 'is_staff', 'is_verified')
  list_filter = ('email', 'is_active',
                 'is_staff', 'account_type')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email',)
  fieldsets = (
      (None, {'fields': ('email', 'password')}),
      ('Personal info', {'fields': (
          'first_name', 'last_name', 'is_verified', 'account_type')}),
      ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
      ('Important dates', {'fields': ('last_login',)}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_superuser'),
      }),
  )
#   readonly_fields = ('date_joined',)


@admin.register(Mechanic)
class MechanicAdmin(gis_admin.OSMGeoAdmin):
  model = Mechanic
  list_display = ('user_profile','mechanic_name',
                  'phone_number','mechanic_nik')
#   list_filter = ('category',)
  search_fields = ('mechanic_name','mechanic_nik')
  ordering = ('mechanic_name',)

  default_zoom = 30

  # def get_queryset(self, request):
  #   return super().get_queryset(request).prefetch_related('category')

  def category_list(self, obj):
    return u", ".join(o.name for o in obj.category.all())


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  model = Customer
  list_display = ('user_profile','user_id', 'phone_number')
  search_fields = ('user_profile__email', 'phone_number')
  ordering = ('user_profile__email',)

  default_zoom = 30
