from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from home.models import App

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from home.forms import AppAddForm


class ApiAppListView(ListView):
    model = App
    template_name = 'home/dashboard/app/app-list.html'


class AddAppView(CreateView):
    model = App
    form_class = AppAddForm
    template_name = 'home/dashboard/app/add-app.html'
    success_url = reverse_lazy('home_page:app_list')

    def form_valid(self, form):
        app = form.save(commit=False)
        app.created_by = self.request.user
        app.save()
        return super().form_valid(form)


class DeleteAppView(DeleteView):
    model = App
    template_name = 'home/dashboard/app/delete-app.html'
    success_url = reverse_lazy('home_page:app_list')

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     print(self)
    #     print(args)
    #     print(kwargs['pk'])
    #     return super().post(request)

class AppEditView(UpdateView):
    model = App
    form_class = AppAddForm
    template_name = 'home/dashboard/app/app-update.html'

    # success_url = reverse_lazy('home_page:category_list')
    def get_success_url(self):
        return self.object.get_absolute_url()