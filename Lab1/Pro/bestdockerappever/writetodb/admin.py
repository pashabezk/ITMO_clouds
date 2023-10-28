from django.contrib import admin

# Register your models here.
from writetodb.models import BootRecord

admin.site.register(BootRecord)