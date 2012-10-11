from django.contrib import admin
from tally.api.models import Client, Counter


class ClientAdmin(admin.ModelAdmin):
    fields = ['app_name', 'user', 'api_key']


admin.site.register(Client, ClientAdmin)
admin.site.register(Counter)
