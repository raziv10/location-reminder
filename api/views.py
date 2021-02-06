from django.shortcuts import render
from .serializers import LocationSerializers
from .models import location
from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
# Create your views here.


class LocationListView(ListAPIView):
    queryset = location.objects.all()
    serializer_class = LocationSerializers
    # lookup_field = 'slug'


class LocationDetailView(RetrieveAPIView):
    queryset = location.objects.all()
    # permission_classes = [AllowAny]
    serializer_class = LocationSerializers


class LocationCreateView(CreateAPIView):
    queryset = location.objects.all()
    serializer_class = LocationSerializers


class LocationDeleteView(DestroyAPIView):
    queryset = location.objects.all()
    serializer_class = LocationSerializers
    # lookup_field = 'slug'


class LocationUpdateView(RetrieveUpdateAPIView):
    queryset = location.objects.all()
    serializer_class = LocationSerializers
    # lookup_field = 'slug'
