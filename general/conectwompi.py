
import requests

# Your Wompi API Key
api_key = 'pub_test_lbyRMfDLL4B502sS0Xtb9J7PvN4gBZs5'

# Your Wompi Merchant ID
merchant_id = 39786

# Your Wompi Secret Key
secret_key = "pub_test_lbyRMfDLL4B502sS0Xtb9J7PvN4gBZs5"

# The amount of the transaction
amount = 1000000

# The currency of the transaction
currency = "COP"

# The description of the transaction
description = "Test Transaction"

# The URL to redirect the user after the transaction is completed
redirect_url = "https://example.com/transaction-complete"

# The URL to notify Wompi when the transaction is completed
notify_url = "https://example.com/transaction-notify"

# Build the request payload
payload = {
    "apiKey": api_key,
    "merchantId": merchant_id,
    "secretKey": secret_key,
    "amount": amount,
    "currency": currency,
    "description": description,
    "redirectUrl": redirect_url,
    "notifyUrl": notify_url
}

# Make the request to the Wompi API
response = requests.post("https://sandbox.wompi.co/v1/transactions", json=payload)

# Print the response
if response.status_code != 204:
    print(response.json())
else:
    'vacio'