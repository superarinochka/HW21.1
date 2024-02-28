from django.urls import path

from catalog.views import ProductListView, ContactDetailView

app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactDetailView.as_view(), name='contacts'),
]