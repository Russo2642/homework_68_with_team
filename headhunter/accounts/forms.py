from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label='Подтвердите пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput
    )
    phone = forms.RegexField(
        regex=r'[^\+?1?\d{9,15}$]',
        error_messages=({'invalid': 'Введите номер телефона в формате +7 777 123 4567. Максимум 15 цифр.'}),
    )

    class Meta:
        model = get_user_model()
        fields = (
            'is_employer',
            'username',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'phone'
        )
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон'
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        if user.is_employer:
            user.groups.add(1)
        else:
            user.groups.add(2)
        user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'avatar', 'phone')
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'avatar': 'Аватар',
            'phone': 'Телефон'
        }
