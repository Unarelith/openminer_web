from django.contrib import admin

from .models import EngineVersion, Mod, ModVersion, TexturePack, TexturePackVersion

class EngineVersionAdmin(admin.ModelAdmin):
    list_display   = ('name', 'date')
    list_filter    = ('name', )
    ordering       = ('name', 'date')
    search_fields  = ('name', )

class ModAdmin(admin.ModelAdmin):
    list_display   = ('name', 'user', 'date')
    list_filter    = ('name', 'user')
    ordering       = ('name', 'user', 'date')
    search_fields  = ('name', 'user')

class ModVersionAdmin(admin.ModelAdmin):
    list_display   = ('mod', 'name', 'date', 'doc')
    list_filter    = ('mod', )
    ordering       = ('mod', 'name', 'date')
    search_fields  = ('mod', 'name')

class TexturePackAdmin(admin.ModelAdmin):
    list_display   = ('name', 'user', 'date')
    list_filter    = ('name', 'user')
    ordering       = ('name', 'user', 'date')
    search_fields  = ('name', 'user')

class TexturePackVersionAdmin(admin.ModelAdmin):
    list_display   = ('texture_pack', 'name', 'date', 'doc')
    list_filter    = ('texture_pack', )
    ordering       = ('texture_pack', 'name', 'date')
    search_fields  = ('texture_pack', 'name')

admin.site.register(EngineVersion, EngineVersionAdmin)
admin.site.register(Mod, ModAdmin)
admin.site.register(ModVersion, ModVersionAdmin)
admin.site.register(TexturePack, TexturePackAdmin)
admin.site.register(TexturePackVersion, TexturePackVersionAdmin)

