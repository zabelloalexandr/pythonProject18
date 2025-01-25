from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label="Введите логин",
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[MaxLengthValidator(30)]
    )

    password = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[MinLengthValidator(8)]
    )

    repeat_password = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[MinLengthValidator(8)]
    )

    age = forms.IntegerField(
        label="Введите свой возраст",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '3'}),
        validators=[MaxLengthValidator(3)]
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        # Проверка совпадения паролей
        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают!")

        return cleaned_data