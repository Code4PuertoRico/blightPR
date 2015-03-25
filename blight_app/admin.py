from django.contrib import admin
from blight_app.models import AbndSite


class AbndSiteAdmin(admin.ModelAdmin):
	model = AbndSite
	list_display = ('catastro', 'lat', 'lng')
	search_fields = ['catastro']


admin.site.register(AbndSite, AbndSiteAdmin)