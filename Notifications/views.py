from django.http import HttpResponse

from .services import my_task

def test_fnc(request):
    my_task()
    return HttpResponse("Done")
