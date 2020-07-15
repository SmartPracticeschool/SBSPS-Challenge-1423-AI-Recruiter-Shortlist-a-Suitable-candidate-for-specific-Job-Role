from django import forms
from recruiter.models import document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = document
        fields = ('document',)
        
class UploadFileForm(forms.Form):
    file = forms.FileField(label='',widget=forms.FileInput(attrs={'style' : 'display:none;','value':'choosefile','placeholder':'choosefile'}))

