from django.contrib import admin

from .models import User, Hotel, Mylist

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Mylist)

# Register your models here.
