from django.urls import path
from personal.views import get_interests, get_hobbies


urlpatterns = [
    path('interests', get_interests),
    path('hobbies', get_hobbies)
]