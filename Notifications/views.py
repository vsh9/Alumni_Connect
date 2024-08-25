from django.http import HttpResponse
from .services import send_general_message, send_rsvp_updates
from Events.models import Event
from .services import TwilioClient

def test_fnc(request):
    client = TwilioClient()
    client.send_buttons_example(to=918792463479)
    return HttpResponse("Done")

def send_message_view(request):
    message = "Hello Alumni! Don't miss our upcoming events."
    send_general_message(message)
    return JsonResponse({'status': 'General message sent'})

def send_update_view(request, event_id):
    event = Event.objects.get(event_id=event_id)
    update_message = "This is a friendly reminder for the event."
    send_rsvp_updates(event, update_message)
    return JsonResponse({'status': 'Update sent to RSVP\'d users'})