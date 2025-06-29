Objective

Integrate the Chapa API for handling payments, allowing users to make bookings with secure payment options. Configure the API to initiate and verify payments and handle the payment status accordingly.

Instructions

Duplicate Project:

Duplicate the project alx_travel_app_0x01 to alx_travel_app_0x02
Set Up Chapa API Credentials:

Create an account with Chapa (https://developer.chapa.co/) to obtain the API keys.
Store the API keys in environment variables for security (CHAPA_SECRET_KEY).
Create Payment Model:

In listings/models.py, create a Payment model to store payment-related information such as booking reference, payment status, amount, and transaction ID.
