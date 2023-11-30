# Billing App
This is Flask app Endpoint

# Test app Endpoint:

- CURL:
   curl -X POST -H "Content-Type: application/json" -d '{
  "senderEmail": "sender@savvytribe.tech",
  "recipientDetails": {"name": "John Doe", "email": "john.doe@savvytribe.tech"},
  "invoiceDetails": {"amount": 100.0, "description": "Invoice for services"},
  "invoiceTemplateId": "template123"
}' http://127.0.0.1:5000/send_invoice

- Postman App:
  curl --location 'http://127.0.0.1:5000/send_invoice' \
--header 'Content-Type: application/json' \
--data-raw '{
    "senderEmail": "sender@savvytribe.tech",
    "recipientDetails": {
        "name": "John Doe",
        "email": "john.doe@savvytribe.tech"
    },
    "invoiceDetails": {
        "amount": 100.0,
        "description": "Invoice for services"
    },
    "invoiceTemplateId": "template2023"
}'

