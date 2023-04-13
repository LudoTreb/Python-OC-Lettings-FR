from django.contrib import admin

from lettings.models import Letting, Address

admin.site.register(Address)
admin.site.register(Letting)
