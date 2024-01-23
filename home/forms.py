from django import forms

from home.models import Category, App


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AppAddForm(forms.ModelForm):
    class Meta:
        model = App
        fields = '__all__'

# class