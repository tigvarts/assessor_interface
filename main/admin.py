from django.contrib import admin
from .models import Query, Mark, CatImage

# Register your models here.

class MarkTabularInline(admin.TabularInline):
    model = Mark

class QueryAdmin(admin.ModelAdmin):
    model = Query
    inlines = [ MarkTabularInline ]

admin.site.register(Query, QueryAdmin)
admin.site.register(Mark)
admin.site.register(CatImage)
