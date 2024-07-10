from app.views import *
from django.urls import path


urlpatterns = [
    # path('', home, name='home'),
    path('', CardList.as_view(), name='home'),
]