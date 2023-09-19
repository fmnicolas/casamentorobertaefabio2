from django.contrib import admin
from .models import Confirmacao
from import_export.admin import ImportExportModelAdmin

class ConfirmacaoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    
admin.site.register(Confirmacao, ConfirmacaoAdmin)