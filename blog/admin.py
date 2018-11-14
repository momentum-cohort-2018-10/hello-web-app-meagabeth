from django.contrib import admin

# import your model
from blog.models import Entry

# set up automated slug creation
class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Entry, EntryAdmin)
