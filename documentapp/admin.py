from django.contrib import admin
from documentapp.models import document
from documentapp.models import functionModel

class documentAdmin(admin.ModelAdmin):
    list_display=('id', 'cClassName', 'cClassDescription', 'cClassOverview',)
    list_filter=('cClassName',)
    search_fields=('cClassName',)
    ordering=('id',)

class functionAdmin(admin.ModelAdmin):
	list_display=('id', 'functionName', 'functionDescription',)
	list_filter=('fdocument',)
	search_fields=('functionName',)
	ordering=('id',)

# Register your models here.
admin.site.register(document, documentAdmin)
admin.site.register(functionModel, functionAdmin)
