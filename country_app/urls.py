from django.urls import path
from .views import CountryList, CountryDetail

urlpatterns = [
    path('country/', CountryList.as_view()), 
    path('country/<int:pk>/', CountryDetail.as_view()), 
]
