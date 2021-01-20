from django.contrib import admin

from acessos.models import Sistema, Acesso, Area

admin.site.register(Sistema)
#admin.site.register(Acesso)
@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    list_display = ('dsMatricula', 'dsUsuario',
                    'dsArea', 'dtUpdate')
    list_filter = ('dsArea', 'dtUpdate')

    fieldsets = (
        ('Usuário', {
            'fields': ('dsMatricula', 'dsUsuario', 'dsArea')
        }),
        ('Acessos', {
            'fields': (['dsSistema'])
        }),
    )


admin.site.register(Area)
