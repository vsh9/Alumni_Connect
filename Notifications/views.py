from django.http import HttpResponse

from .services import TwilioClient

def test_fnc(request):
    client = TwilioClient()
    client.send_buttons_example(to=918792463479)
    return HttpResponse("Done")
