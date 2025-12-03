from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Client, Domain, User
# Register your models here.


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'created_on', 'schema_name')
    search_fields = ('name', 'schema_name')

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    search_fields = ('domain',)
