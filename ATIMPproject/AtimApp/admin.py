from django.contrib import admin
from .models import University, Company, Graduete_Students, Job_Offer


# Register your models here.
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'city')
    list_filter = ('name', 'city')
    search_fields = ('name', 'city')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'city')
    list_filter = ('name', 'city')
    search_fields = ('name', 'city')


class Graduete_StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'major', 'GPA', 'graduete_date', 'university')
    list_filter = ('major', 'GPA')
    date_hierarchy = ('graduete_date')
    search_fields = ('major', 'GPA')


class Job_OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'company', 'student', 'isAccepted')
    list_filter = ('name', 'student', 'company', 'isAccepted')
    search_fields = ('isAccepted', 'student', 'company')


admin.site.register(University, UniversityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Graduete_Students, Graduete_StudentsAdmin)
admin.site.register(Job_Offer)
