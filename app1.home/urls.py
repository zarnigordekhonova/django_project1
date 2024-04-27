from django.urls import path
from home.views import get_info, get_university_info

urlpatterns = [
    path('app_url', get_info),
    path('university', get_university_info)
]