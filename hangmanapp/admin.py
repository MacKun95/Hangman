from django.contrib import admin

from hangmanapp.models import AktivWord, GameWords, ListItem, Player

# Register your models here.
admin.site.register(ListItem)
admin.site.register(GameWords)
admin.site.register(Player)
admin.site.register(AktivWord)
