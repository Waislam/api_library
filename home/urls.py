from django.urls import path
from .views.api import (HomePageView,
                        DashboardIndex,
                        ApiListView,
                        AddApiView,
                        DeleteApiView, ApiEditView
                        )

from .views.category import (
    ApiCategoryListView,
    AddCategoryView,
    CategoryDeleteView,
    CategoryEditView
)
from .views.app import (ApiAppListView,
                        AddAppView,
                        DeleteAppView,
                        AppEditView,
                        )

app_name = 'home_page'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # api library view
    # dashboard home
    path('dashboard/', DashboardIndex.as_view(), name='dashboard'),
    # api
    path('dashboard/api/api-list/', ApiListView.as_view(), name='api_list'),
    path('dashboard/api/add-api/', AddApiView.as_view(), name='add_api'),
    path('dashboard/api/api/delete/<int:pk>/', DeleteApiView.as_view(), name='del_api'),
    path('dashboard/api/api/update/<int:pk>/', ApiEditView.as_view(), name='api_update'),
    # category
    path('dashboard/api/category/', ApiCategoryListView.as_view(), name='category_list'),
    path('dashboard/api/add-category/', AddCategoryView.as_view(), name='add_category'),
    path('dashboard/api/category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='cat_del'),
    path('dashboard/api/category/update/<int:pk>/', CategoryEditView.as_view(), name='cat_update'),
    # app
    path('dashboard/api/app/', ApiAppListView.as_view(), name='app_list'),
    path('dashboard/api/add-app/', AddAppView.as_view(), name='add_app'),
    path('dashboard/api/app/delete/<int:pk>/', DeleteAppView.as_view(), name='del_app'),
    path('dashboard/api/app/update/<int:pk>/', AppEditView.as_view(), name='app_update'),

]
