from django import forms

class LoginForm(forms.Form):

    nome_login = forms.CharField(
        label= 'Nome de login',
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'seu login nesse campo',
            }
        )
    )

    senha = forms.CharField(
        label= 'Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'sua senha nesse campo',

            }
        )

    )
