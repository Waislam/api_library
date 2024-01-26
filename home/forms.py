from django import forms

from home.models import Category, App, Api


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AppAddForm(forms.ModelForm):
    class Meta:
        model = App
        fields = '__all__'


class ApiAddForm(forms.ModelForm):
    class Meta:
        model = Api
        fields = '__all__'
