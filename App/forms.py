import re
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Application, Review


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150, label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Логин (лат. буквы и цифры, мин. 6)'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль (мин. 8 символов)'})
    )
    confirm_password = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повторите пароль'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'example@mail.ru'})
    )
    fio = forms.CharField(
        max_length=255, label='ФИО',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Иванов Иван Иванович'})
    )
    birth_date = forms.DateField(
        label='Дата рождения',
        input_formats=['%d.%m.%Y'],
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'ДД.ММ.ГГГГ'})
    )
    phone = forms.CharField(
        max_length=20, label='Телефон',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+7 (999) 123-45-67'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise forms.ValidationError('Логин должен содержать минимум 6 символов')
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError('Логин должен содержать только латинские буквы и цифры')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким логином уже существует')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Пароль должен содержать минимум 8 символов')
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data['confirm_password']
        if password and password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return confirm_password

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        Profile.objects.create(
            user=user,
            fio=self.cleaned_data['fio'],
            birth_date=self.cleaned_data['birth_date'],
            phone=self.cleaned_data['phone']
        )
        return user


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['transport_type', 'start_date', 'payment_method']
        widgets = {
            'transport_type': forms.Select(attrs={'class': 'form-input'}),
            'start_date': forms.DateInput(
                attrs={'class': 'form-input', 'placeholder': 'ДД.ММ.ГГГГ'},
                format='%d.%m.%Y'
            ),
            'payment_method': forms.Select(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['transport_type'].label = 'Вид транспорта'
        self.fields['start_date'].label = 'Дата начала обучения'
        self.fields['payment_method'].label = 'Способ оплаты'
        self.fields['start_date'].input_formats = ['%d.%m.%Y']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Напишите ваш отзыв...',
                'rows': 4
            }),
        }
        labels = {
            'text': 'Ваш отзыв',
        }
