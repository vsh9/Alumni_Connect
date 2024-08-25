from django.contrib import admin
from django.urls import path
from Alumni.apis import app
from Notifications.apis import notify
from Events.apis import eve
from ninja import NinjaAPI
from django.http import HttpResponse
from Notifications.views import send_message_view, send_update_view


api = NinjaAPI()
def home(request):
    return HttpResponse("Welcome to IISC Alumni Association")

api.add_router('alumni/', app)
api.add_router('notifications/', notify)
api.add_router('events/',eve)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('send-general-message/', send_message_view, name='send_general_message'),
    path('send-update/<int:event_id>/', send_update_view, name='send_update'),
    path('api/',api.urls)
]
