from django.contrib import admin
from django.urls import path
from Notifications.apis import notify
from Events.apis import eve
from django.http import HttpResponse

def home(request):
    return HttpResponse("WhatsApp API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', notify.urls),
    path('events/',eve.urls),
    path('', home),
]
