import requests
from config.settings import Config

class WhatsAppClient:
    @staticmethod
    def send_message(to_number, text_body):
        url = f"https://graph.facebook.com/v18.0/{Config.PHONE_NUMBER_ID}/messages"
        headers = {
            "Authorization": f"Bearer {Config.WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": to_number,
            "type": "text",
            "text": {"body": text_body}
        }
        
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"WhatsApp API Error: {response.text}")
            return False
        print(f"Message sent to {to_number}")
        return True