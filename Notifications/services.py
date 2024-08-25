from twilio.rest import Client
from django.conf import settings
from main import settings
from Events.models import EventAlumni,Event
from Alumni.models import alumni
import json

class TwilioClient:
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def send_rsvp_confirmation(self, al: alumni):
        message_data = {
            'content_sid':'HX8472c88688bb676a1f29b1d31f7d82ee',
            'from_': f'whatsapp:+{settings.TWILIO_WHATSAPP_NUMBER}',
            'to': f'whatsapp:+{al.phone_number}',
            'content_variables': json.dumps({"1": f"{al.first_name}"})
        }
        message = self.client.messages.create(**message_data)
        return message.sid

#Send general message to user
    def send_general_message(self, message):
        alumni_list = alumni.objects.all()
        
        for al in alumni_list:
            self.client.messages.create(
                body=message,
                from_=f'whatsapp:+{settings.TWILIO_WHATSAPP_NUMBER}',
                to=f'whatsapp:+{al.phone_number}'
            )
            self.send_rsvp_confirmation(al=al)


#Send message to user who has accepted RSVP for an event
    def send_rsvp_updates(self,eve: Event, update_message):
        EA=EventAlumni.objects.all().filter(event_id=eve.event_id)

        for rsvp in EA:
            a = rsvp.alumni_id
            self.client.messages.create(
                body=f"Update for {eve.event_name}: {update_message}",
                from_=f'whatsapp:+{settings.TWILIO_WHATSAPP_NUMBER}',
                to=f'whatsapp:+{a.phone_number}'
            )
