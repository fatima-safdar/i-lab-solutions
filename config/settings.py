import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
    PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "ilabsolution_secret_token")
    PORT = int(os.getenv("PORT", 5000))

    # Twilio WhatsApp settings
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER", "whatsapp:+14155238886")
