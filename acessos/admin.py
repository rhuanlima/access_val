from django.contrib import admin

from acessos.models import Sistema, Acesso, Area, SystemInstance

import datetime
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE


class MoniterLog(admin.ModelAdmin):
    list_display=(
        'action_time',
        'user',
        'content_type',
        'object_repr',
        'change_message',
        'action_flag'
    )
    list_filter=[
        'action_time',
        'user',
        'content_type'
    ]
    ordering=('-action_time',)

admin.site.register(LogEntry, MoniterLog)

admin.site.register(Sistema)

@admin.register(SystemInstance)
class SystemInstanceAdmin(admin.ModelAdmin):
    pass


class SystemInstanceInline(admin.TabularInline):
    model = SystemInstance
    list_display = ('dsSistema', 'dsObs', 'dsStatus')
    verbose_name = "Acesso"
    verbose_name_plural = "Meus acessos"
    


#admin.site.register(Acesso)

@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    list_display = ('dsMatricula', 'dsUsuario', 'dsUserEmail',
                    'dsArea', 'dtUpdate', 'get_profile')
    list_filter = ('dsArea', 'dtUpdate')

    fieldsets = (
        ('Usuário', {
            'fields': ('dsMatricula', 'dsUsuario', 'dsUserEmail', 'dsArea')
        }),
    )
    inlines = [SystemInstanceInline]



admin.site.register(Area)
#admin.site.register(SystemInstance)

