from django import forms

class TemplateForm(forms.Form):
    my_text = forms.CharField()
    my_email = forms.EmailField()
    my_message = forms.CharField(widget=forms.Textarea)

