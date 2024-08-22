from http.client import HTTPException
from ninja import NinjaAPI
from Alumni.models import Alumni
from Events.models import Event
from .models import NTF
from .schemas import NTFSchemaIn, NTFSchemaOut
from django.shortcuts import get_object_or_404
from typing import List

notify = NinjaAPI(urls_namespace='otherapi')

@notify.get("/notifications", response=List[NTFSchemaOut])
def list_notifications(request):
    return list(NTF.objects.all())

@notify.post("/notifications", response=NTFSchemaOut)
def create_notification(request, payload: NTFSchemaIn):
    event = Event.objects.get(event_id=payload.event_id)
    notification = NTF.objects.create(
        N_id=payload.N_id,
        event_id=event, 
        N_type=payload.N_type,
        N_content=payload.N_content,
        Priority=payload.Priority
    )

    return {
        "N_id": notification.N_id,
        "event_id": notification.event_id.event_id,
        "N_type": notification.N_type,
        "N_content": notification.N_content,
        "Priority": notification.Priority,
    }

@notify.get("/notifications/{notification_id}", response=NTFSchemaOut)
def get_notifications(request, notification_id: int):
    notification = NTF.objects.get(pk=notification_id)
    return notification

@notify.put("/notifications/{notification_id}", response=NTFSchemaOut)
def update_notifications(request, notification_id: int, payload: NTFSchemaIn):
    notification = NTF.objects.get(pk=notification_id)
    event =  Event.objects.get(event_id=payload.event_id)
    payload.event_id = event
    for attr, value in payload.dict().items():
        setattr(notification, attr, value)
    notification.save()
    
    return {
        "N_id": notification.N_id,
        "Event_id": event.event_id,
        "N_type": notification.N_type,
        "N_content": notification.N_content,
        "Priority": notification.Priority,
    }

@notify.delete("/notifications/{notification_id}", response=dict)
def delete_notifications(request, notification_id: int):
    notification = NTF.objects.get(pk=notification_id)
    notification.delete()
    return {"success": True}