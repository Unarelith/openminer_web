from django.contrib import admin

from .models import Mod, ModVersion, TexturePack, TexturePackVersion

class ModAdmin(admin.ModelAdmin):
    list_display   = ('name', 'user')
    list_filter    = ('name', 'user')
    ordering       = ('name', 'user')
    search_fields  = ('name', 'user')

class ModVersionAdmin(admin.ModelAdmin):
    list_display   = ('mod', 'version', 'date', 'doc')
    list_filter    = ('mod', )
    ordering       = ('mod', 'version', 'date')
    search_fields  = ('mod', 'version')

class TexturePackAdmin(admin.ModelAdmin):
    list_display   = ('name', 'user')
    list_filter    = ('name', 'user')
    ordering       = ('name', 'user')
    search_fields  = ('name', 'user')

class TexturePackVersionAdmin(admin.ModelAdmin):
    list_display   = ('texture_pack', 'version', 'date', 'doc')
    list_filter    = ('texture_pack', )
    ordering       = ('texture_pack', 'version', 'date')
    search_fields  = ('texture_pack', 'version')

admin.site.register(Mod, ModAdmin)
admin.site.register(ModVersion, ModVersionAdmin)
admin.site.register(TexturePack, TexturePackAdmin)
admin.site.register(TexturePackVersion, TexturePackVersionAdmin)

