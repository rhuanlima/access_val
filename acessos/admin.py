from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import admin
from acessos.models import Sistema, Acesso, Area, Rede, SistemaExterno
import datetime
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE


class MoniterLog(admin.ModelAdmin):
    list_display = (
        'action_time',
        'user',
        'content_type',
        'object_repr',
        'change_message',
        'action_flag'
    )
    list_filter = [
        'action_time',
        'user',
        'content_type'
    ]
    ordering = ('-action_time',)


admin.site.register(LogEntry, MoniterLog)
admin.site.register(Sistema)
admin.site.register(Rede)
admin.site.register(SistemaExterno)
admin.site.register(Area)
# admin.site.register(Acesso)


@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    list_display = ('dsMatricula', 'dsUserWeb', 'dsUsuario', 'dsUserEmail',
                    'dsArea', 'dtUpdate', 'get_access')
    list_filter = ('dsArea', 'dtUpdate')

    fieldsets = (
        ('Usuário', {
            'fields': ('dsMatricula', 'dsUserWeb', 'dsUsuario', 'dsUserEmail',
                       'dsArea', 'dsSistema', 'dsSistemaExterno', 'dsRede')
        }),
    )
    filter_horizontal = ['dsSistema', 'dsSistemaExterno', 'dsRede']

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/acessos/list')

    def response_change(self, request, obj):
        return redirect('/acessos/list')


