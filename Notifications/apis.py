from http.client import HTTPException
from ninja import NinjaAPI
from Alumni.models import alumni
from Events.models import Event
from .models import Notification
from .schemas import NTFSchemaIn, NTFSchemaOut
from django.shortcuts import get_object_or_404
from typing import List

notify = NinjaAPI(urls_namespace='otherapi')

@notify.get("/notifications", response=List[NTFSchemaOut])
def list_notifications(request):
    return list(Notification.objects.all())

@notify.post("/notifications", response=NTFSchemaOut)
def create_notification(request, payload: NTFSchemaIn):
    event = Event.objects.get(event_id=payload.event_id)
    notification = Notification.objects.create(
        n_id=payload.n_id,
        event_id=event, 
        n_type=payload.n_type,
        n_content=payload.n_content,
        priority=payload.priority
    )

    return {
        "n_id": notification.n_id,
        "event_id": notification.event_id.event_id,
        "n_type": notification.n_type,
        "n_content": notification.n_content,
        "priority": notification.priority,
    }

@notify.get("/notifications/{notification_id}", response=NTFSchemaOut)
def get_notifications(request, notification_id: int):
    notification = Notification.objects.get(pk=notification_id)
    return notification

@notify.put("/notifications/{notification_id}", response=NTFSchemaOut)
def update_notifications(request, notification_id: int, payload: NTFSchemaIn):
    notification = Notification.objects.get(pk=notification_id)
    event =  Event.objects.get(event_id=payload.event_id)
    payload.event_id = event
    for attr, value in payload.dict().items():
        setattr(notification, attr, value)
    notification.save()
    
    return {
        "n_id": notification.n_id,
        "event_id": event.event_id,
        "n_type": notification.n_type,
        "n_content": notification.n_content,
        "priority": notification.priority,
    }

@notify.delete("/notifications/{notification_id}", response=dict)
def delete_notifications(request, notification_id: int):
    notification = Notification.objects.get(pk=notification_id)
    notification.delete()
    return {"success": True}