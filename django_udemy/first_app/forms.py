from django import forms
from django.core import validators
from first_app.models import User
from django.forms import ModelForm
# def check_for_a(value):
#     if value[0].lower() != 'a':
#         raise forms.ValidationError("Start with z")

# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_a])
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label="Enter your email")
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required = False,
#                                 widget=forms.HiddenInput,
#                                 validators = [validators.MaxLengthValidator(0)])
    
#     def clean(self):
#         all_cleaned_data = super().clean()
#         email = all_cleaned_data['email']
#         vemail = all_cleaned_data['verify_email']

#         if email != vemail:
#             raise forms.ValidationError("both has to be same")

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = "__all__"


    # botcatcher = forms.CharField(widget=forms.HiddenInput,
    #                             required = "False")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']

    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return botcatcher
