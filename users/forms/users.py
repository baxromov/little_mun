from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'message': 'Should complete this field'})
    first_name = forms.CharField(required=True, error_messages={'message': 'Should complete this field'})
    last_name = forms.CharField(required=True, error_messages={'message': 'Should complete this field'})
    email = forms.EmailField(required=True, error_messages={'message': 'Should complete this field'})
    password1 = forms.CharField(required=True, error_messages={'message': 'Should complete this field'})
    password2 = forms.CharField(required=True, error_messages={'message': 'Should complete this field'})

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Password 1 not equal to Password 2')
        return self.cleaned_data
