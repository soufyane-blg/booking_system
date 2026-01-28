from django import forms
from .models import Booking
from datetime import date as today_date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta :
        model = User
        fields = ['username', 'email', 'password']


class BookingForm(forms.ModelForm):
    class Meta:   
        model = Booking
        fields = ['service', 'date', 'time']

    def clean_date(self):
           
        date = self.cleaned_data.get('date')

        if date and date < today_date.today():
            raise forms.ValidationError(
                "You cannot book a date in the past."
            )

        return date

    def clean(self):
                
        cleaned_data = super().clean()

        service = cleaned_data.get('service')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if service and date and time:
            exists = Booking.objects.filter(
                service=service,
                date=date,
                time=time
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "This service is already booked at this time."
                )

        return cleaned_data