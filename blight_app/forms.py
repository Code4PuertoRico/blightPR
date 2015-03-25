from django import forms
from blight_app.models import AbndSite


class AbndSiteForm(forms.ModelForm):
	catastro = forms.CharField(max_length=128)
	lat = forms.CharField(max_length=128, required=False)
	lng = forms.CharField(max_length=128, required=False)

	dueno = forms.CharField(max_length=128, required=False)	
	calle = forms.CharField(max_length=128, required=False)
	numero = forms.CharField(max_length=128, required=False)
	comunidad = forms.CharField(max_length=128, required=False)
	cabida = forms.CharField(max_length=128, required=False)
	tenencia = forms.CharField(max_length=128, required=False)
	tipo = forms.CharField(max_length=128, required=False)
	calificacion = forms.CharField(max_length=128, required=False)
	descripcion = forms.CharField(max_length=128, required=False)
	inundabilidad = forms.CharField(max_length=128, required=False)

	v_estructura = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
	v_solar = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
	v_total = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)

	comentarios = forms.CharField(widget=forms.Textarea, required=False)
	
	class Meta:
		model = AbndSite
        exclude = ('v_estructura', 'v_solar', 'v_total',)