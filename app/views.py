from django.shortcuts import render
from django.views.generic import ListView

from app.models import Card

# Create your views here.

# def home(request):
#     return render(request, 'home.html')

class CardList(ListView):
    queryset = Card.objects.all()
    template_name = 'home.html'