from django.db import models
from django.urls import reverse

from core.global_models import TimeStampMixin
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class App(TimeStampMixin):
    app_name = models.CharField(max_length=255)
    # parent_app = models.
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='home_app_related', blank=True,
                                   null=True)

    def __str__(self):
        return self.app_name

    def get_absolute_url(self):
        return reverse('home_page:app_list')


class Category(TimeStampMixin):
    category_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='home_category_related', blank=True,
                                   null=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('home_page:category_list')


class Api(TimeStampMixin):
    TYPE_CHOICE = [
        ('get', 'GET'),
        ('post', 'POST'),
        ('put', 'PUT'),
        ('patch', 'PATCH'),
        ('delete', 'DELETE'),
    ]
    key = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255)
    unique_code = models.CharField(max_length=20, unique=True)  # auto generated from backend
    category = models.ManyToManyField(Category, related_name='home_api_cat_related')
    app = models.ForeignKey(App, on_delete=models.SET_NULL, related_name='home_api_app_related', blank=True, null=True)
    api_url = models.CharField(max_length=500)
    api_type = models.CharField(max_length=10, choices=TYPE_CHOICE, default='GET')
    description = models.TextField(max_length=1500)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='home_api_related', blank=True,
                                   null=True)

    def __str__(self):
        return self.unique_code
