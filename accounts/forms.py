from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username or Email',
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username',
            'class': 'thq-input thq-body-large sign-in32-textinput1'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'thq-input thq-body-large sign-in32-textinput2'
        })
    )