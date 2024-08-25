from django.contrib import admin
from django.urls import path
from Alumni.apis import app
from Notifications.apis import notify
from Events.apis import eve
from MessageLog.api import router as ml_router
from django.http import HttpResponse
from Notifications.views import test_fnc,send_message_view, send_update_view

def home(request):
    return HttpResponse("Welcome to IISC Alumni Association")

# api.add_router("/ml/", ml_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alumni/', app.urls),
    path('notifications/', notify.urls),
    path('events/',eve.urls),
    path('', home),
    path('ml/',ml_router.urls),
    path('test/',test_fnc),
    path('send-general-message/', send_message_view, name='send_general_message'),
    path('send-update/<int:event_id>/', send_update_view, name='send_update'),
]
