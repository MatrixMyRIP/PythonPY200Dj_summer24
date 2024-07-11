from django import forms

class TemplateForm(forms.Form):
    my_text = forms.CharField()
    my_email = forms.EmailField()
    my_message = forms.CharField(widget=forms.Textarea)


# def ip_user(self, request):
#     my_text = self.cleaned_data['my_text']
#     my_email = self.cleaned_data['my_email']
#     my_message = self.cleaned_data['my_message']
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]  # Получение IP
#     else:
#         ip = request.META.get('REMOTE_ADDR')  # Получение IP
#
#     user_agent = request.META.get('HTTP_USER_AGENT')

