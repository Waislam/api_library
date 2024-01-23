from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic.list import ListView

from home.models import Api


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/index.html/', {})


class DashboardIndex(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/dashboard/index-body.html', {})


class ApiListView(ListView):
    template_name = 'home/dashboard/api/api-list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class AddApiView(CreateView):
    """don't use View rather use CreateView to add obj to model ... do it affter creating model """
    model = Api
    template_name = 'home/dashboard/api/add-api.html'
    success_url = reverse_lazy('home_page:api_list')
