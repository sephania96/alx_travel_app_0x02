from django.shortcuts import render
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
import requests
from django.conf import settings
from django.http import JsonResponse
from listings.models import Payment
import uuid
# Create your views here.

class ListingViewSet(viewsets.ModelViewSet):
    """Handles CRUD for listings."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """Handles CRUD for bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def initiate_payment(request):
    transaction_id = str(uuid.uuid4())
    chapa_url = 'https://api.chapa.co/v1/transaction/initialize'
    
    payload = {
        'amount': '100',
        'currency': 'ETB',
        'email': 'customer@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'tx_ref': transaction_id,
        'callback_url': 'https://yourdomain.com/verify-payment/',
        'return_url': 'https://yourdomain.com/success/',
        'customization[title]': 'Booking Payment',
        'customization[description]': 'Payment for your booking',
    }

    headers = {
        'Authorization': f'Bearer {settings.CHAPA_SECRET_KEY}',
    }

    response = requests.post(chapa_url, json=payload, headers=headers)
    data = response.json()

    if response.status_code == 200 and data.get('status') == 'success':
        Payment.objects.create(
            booking_reference=transaction_id,
            transaction_id=transaction_id,
            amount=100,
            status='Pending',
            email='customer@example.com'
        )
        return JsonResponse(data['data'])
    return JsonResponse({'error': 'Failed to initiate payment'}, status=400)
