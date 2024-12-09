from django.shortcuts import render
from .models import FeatureCard


def index(request):
    cards = FeatureCard.objects.all()
    return render(request, 'site_app/index.html', {'cards': cards})
