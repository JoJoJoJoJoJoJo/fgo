from django.contrib import admin
from .models import *


class ServantAdmin(admin.ModelAdmin):
    list_display = ('name','classes','stars','nick','features')
    list_filter = ('classes','stars','features')
    search_fields = ('name','classes','stars','nick')
    ordering = ('name',)

admin.site.register(Servant,ServantAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','nick')
    search_fields = ('name',)

admin.site.register(Item,ItemAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name','quality','cd')
    ordering = ('name',)
    search_fields = ('name',)

admin.site.register(Skill,SkillAdmin)


class LvlupAdmin(admin.ModelAdmin):
    list_display = ('times',)
    ordering = ('times',)

admin.site.register(Lvlup,LvlupAdmin)


class SkillDetailAdmin(admin.ModelAdmin):
    list_display = ('skill','level','rate_or_number')
    ordering = ('skill',)
    search_fields = ('skill',)

admin.site.register(SkillDetail,SkillDetailAdmin)


class PhantasmLevelDetailAdmin(admin.ModelAdmin):
    list_display = ('phantasm','rate_or_number')
    ordering = ('phantasm',)
    search_fields = ('phantasm',)

admin.site.register(PhantasmLevelDetail,PhantasmLevelDetailAdmin)
admin.site.register(PhantasmOcDetal,PhantasmLevelDetailAdmin)


class PhantasmAdmin(admin.ModelAdmin):
    list_display = ('servant','name','p_type')
    ordering = ('name',)
    search_fields = ('name','servant')

admin.site.register(Phantasm,PhantasmAdmin)


class NegativeSkillAdmin(admin.ModelAdmin):
    list_display = ('servant','name','quality')
    search_fields = ('servant','name')

admin.site.register(NegativeSkill,NegativeSkillAdmin)


class SkillItemAmountAdmin(admin.ModelAdmin):
    list_display = ('skill','amount',)

admin.site.register(SkillItemAmount,SkillItemAmountAdmin)


class SkillLevelAdmin(admin.ModelAdmin):
    list_display = ('servant','level')

admin.site.register(SkillLevel,SkillLevelAdmin)


class LvlupItemAmountAdmin(admin.ModelAdmin):
    list_display = ('lvlup','item','amount')
    search_fields = ('lvlup','item')

admin.site.register(LvlupItemAmount,LvlupItemAmountAdmin)