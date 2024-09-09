from django.contrib import admin
from django.urls import path
from Alumni.apis import app
from Notifications.apis import notify
from Events.apis import eve
from ninja import NinjaAPI
from django.http import HttpResponse
from Notifications.views import bot


api = NinjaAPI()
def home(request):
    return HttpResponse("Welcome to IISC Alumni Association")

api.add_router('alumni/', app)
api.add_router('notifications/', notify)
api.add_router('events/',eve)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('api/',api.urls),
    path('',bot)
]
