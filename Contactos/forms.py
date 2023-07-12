from django import forms

class FormularioContacto(forms.Form):

    asunto=forms.CharField(label="Asunto:", required=True)

    contenido=forms.CharField(label="Contenido:", widget=forms.Textarea, required=True)

    adjunto=forms.CharField(label="Adjunto:", required=True)