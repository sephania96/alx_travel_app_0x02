from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
    path('pay/', views.initiate_payment, name='initiate_payment'),
    path('verify-payment/<str:tx_ref>/', views.verify_payment, name='verify_payment'),
]