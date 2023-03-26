from django import forms
from django.core import validators

class ElectronicsRegistration(forms.Form):
    first_name = forms.CharField()
   # first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your First Name"} ))
    last_name = forms.CharField()
    email = forms.EmailField(validators=[validators.MaxLengthValidator(20)])
    batch = forms.IntegerField(help_text="Must fil the bathc")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Enter Your Password"}), min_length=8, max_length= 15)
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Enter Your Password"}), min_length=8, max_length= 15)
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols': 20}), error_messages= {'required': 'Please fill up textarea'})
    rollno = forms.IntegerField( label='Class Roll ', required=False)
    payment = forms.DecimalField(min_value=2500, max_value= 5000, max_digits=6, decimal_places=2)
    django = forms.BooleanField()


    def clean(self):
        cleaned_data = super().clean()
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']
        if password_match != re_password_match:
            raise forms.ValidationError('Confirm password dose not matched !!!')
        



    