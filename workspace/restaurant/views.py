from django.shortcuts import render
from .models import MenuItem, Booking
from .serializers import BookingSerializer, MenuItemSerializer, UserSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated] 