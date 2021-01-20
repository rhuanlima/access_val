from django.contrib import admin

from acessos.models import Sistema, Acesso, Area, SystemInstance

#admin.site.register(Sistema)


@admin.register(SystemInstance)
class SystemInstanceAdmin(admin.ModelAdmin):
    pass


class SystemInstanceInline(admin.TabularInline):
    model = SystemInstance
    list_display = ('dsSistema', 'dsStatus')
    


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
    )
    inlines = [SystemInstanceInline]



admin.site.register(Area)
#admin.site.register(SystemInstance)

