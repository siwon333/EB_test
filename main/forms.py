# main/forms.py
from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'expiration_date']  # 음식 이름과 유통기한 필드
