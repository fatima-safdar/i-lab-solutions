from twilio.rest import Client
from config.settings import Config


class WhatsAppClient:
    @staticmethod
    def send_message(to_number, text_body):
        """
        Send an outbound WhatsApp message via Twilio.
        to_number should be in the format: whatsapp:+92xxxxxxxxxx
        """
        try:
            client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

            if not to_number.startswith("whatsapp:"):
                to_number = f"whatsapp:{to_number}"

            message = client.messages.create(
                from_=Config.TWILIO_WHATSAPP_NUMBER,
                to=to_number,
                body=text_body
            )
            print(f"Message sent to {to_number}, SID: {message.sid}")
            return True
        except Exception as e:
            print(f"Twilio API Error: {e}")
            return False
