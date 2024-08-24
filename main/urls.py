from django.contrib import admin
from django.urls import path
from Alumni.apis import app
from Notifications.apis import notify
from Events.apis import eve
from django.http import HttpResponse
from Notifications.views import test_fnc

def home(request):
    return HttpResponse("Welcome to IISC Alumni Association")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumni/', app.urls),
    path('notifications/', notify.urls),
    path('events/',eve.urls),
    path('', home),
    path('test/',test_fnc),
]
