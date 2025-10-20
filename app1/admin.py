from django.contrib import admin
from app1.models import Stundents
# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display=['id','srollno','sname','sphoneno','sm1','sm2','sm3']
admin.site.register(Stundents,StudentsAdmin)