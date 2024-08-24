from typing import List
from ninja import NinjaAPI
from .schemas import EventSchemaIn, EventSchemaOut
from .models import Event
#import json



eve = NinjaAPI(urls_namespace='eventapi')

@eve.post("/events/", response=EventSchemaOut)
def create_event(request, payload: EventSchemaIn):
    event = Event.objects.create(**payload.dict())
    return {
        "event_id": event.event_id,
        "event_name": event.event_name,
        "event_date_time": event.event_date_time.isoformat(),
        "location": event.location,
        "event_type": event.event_type
    }

@eve.get("/events/", response=List[EventSchemaOut])
def list_events(request):
    events = Event.objects.all()
    return events

@eve.get("/events/{event_id}", response=EventSchemaOut)
def get_event(request, event_id: int):
    event =  Event.objects.get(event_id=event_id)
    return event

@eve.put("/events/{event_id}/", response=EventSchemaOut)
def update_event(request, event_id: int, payload: EventSchemaIn):
    event = Event.objects.get(event_id=event_id)
    for attr, value in payload.dict().items():
        setattr(event, attr, value)
    setattr(event,'event_id',event_id)
    event.save()
    return {
        "event_id": event.event_id,
        "event_name": event.event_name,
        "event_date_time": event.event_date_time.isoformat(),
        "location": event.location,
        "event_type": event.event_type
    }

@eve.delete("/events/{event_id}/")
def delete_event(request, event_id: int):
    event = Event.objects.get(event_id=event_id)
    event.delete()
    return {"success": True}
