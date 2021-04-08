from django.contrib import admin
from .models import PersonalDetail, AddressDetail
# Register your models here.
admin.site.register(PersonalDetail)
admin.site.register(AddressDetail)