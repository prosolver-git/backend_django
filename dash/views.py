from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import DashSerializer      # add this
from .models import Dash                     # add this

# Create your views here.


class DashView(viewsets.ModelViewSet):       # add this
  serializer_class = DashSerializer          # add this
  queryset = Dash.objects.all()              # add this