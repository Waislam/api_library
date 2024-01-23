from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from home.forms import CategoryAddForm
from home.models import Category


class ApiCategoryListView(ListView):
    '''category list view'''
    template_name = 'home/dashboard/category/category-list.html'
    model = Category


class AddCategoryView(View):
    '''category add view'''

    def get(self, request, *args, **kwargs):
        return render(request, 'home/dashboard/category/add-category.html', {})

    def post(self, request, *args, **kwargs):
        # print('myrequest', request.POST)
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('home_page:category_list')
        return render(request, 'home/dashboard/category/add-category.html', {'form': form})


class CategoryDeleteView(DeleteView):
    '''category delete view'''
    model = Category
    template_name = 'home/dashboard/category/category-del.html'
    success_url = reverse_lazy('home_page:category_list')


class CategoryEditView(UpdateView):
    model = Category
    form_class = CategoryAddForm
    template_name = 'home/dashboard/category/update.html'

    # success_url = reverse_lazy('home_page:category_list')
    def get_success_url(self):
        return self.object.get_absolute_url()
