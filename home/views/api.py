from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from home.forms import ApiAddForm
from home.models import Api, App, Category


class HomePageView(ListView):
    model = Api
    template_name = 'home/index.html/'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print("context", context['paginator'])
        # print(context['paginator'].__dict__)
        # Example for a Django instance
        # attributes_only = [attr for attr in dir(context['paginator']) if
        #                    not callable(getattr(context['paginator'], attr)) and not attr.startswith("__")][-2]
        print(context)
        # print('type', type(context['paginator']))

        print('contains', dir(context['paginator']))
        print(context['page_obj'].start_index())

        return context


class DashboardIndex(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/dashboard/index-body.html', {})


class ApiListView(ListView):
    model = Api
    template_name = 'home/dashboard/api/api-list.html'

    def get_queryset(self):
        queryset = Api.objects.filter_by_user(self.request.user.id)
        return queryset



class AddApiView(CreateView):
    """don't use View rather use CreateView to add obj to model ... do it affter creating model """
    model = Api
    form_class = ApiAddForm
    template_name = 'home/dashboard/api/add-api.html'
    success_url = reverse_lazy('home_page:api_list')

    def generate_unique_code(self):
        last_obj = Api.objects.last()
        uni_code = 0
        if last_obj == None:
            uni_code = '1001'
            return uni_code
        else:
            uni_code = last_obj.unique_code
            return str(int(uni_code) + 1)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_unique_code'] = self.generate_unique_code()
        context['app_list'] = App.objects.all()
        context['category_list'] = Category.objects.all()
        context['type_list'] = Api.TYPE_CHOICE
        # print(context)
        return context

    def form_valid(self, form):
        # Assign the current logged-in user to the created object
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class DeleteApiView(DeleteView):
    model = Api
    template_name = 'home/dashboard/api/delete-api.html'
    success_url = reverse_lazy('home_page:api_list')


class ApiEditView(UpdateView):
    model = Api
    form_class = ApiAddForm
    template_name = 'home/dashboard/api/update-api.html'

    success_url = reverse_lazy('home_page:api_list')
    # def get_success_url(self):
    #     return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_list'] = App.objects.all()
        context['category_list'] = Category.objects.all()
        context['type_list'] = Api.TYPE_CHOICE
        # print(context)
        return context