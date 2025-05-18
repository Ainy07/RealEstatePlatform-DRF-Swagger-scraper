from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Property
from .serializers import PropertySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all().order_by('-listed_date')
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    filterset_fields = ['location', 'price']
    search_fields = ['title', 'description']

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]