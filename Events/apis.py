from typing import List
from ninja import NinjaAPI
from .schemas import EventSchema
from .models import Event


eve = NinjaAPI(urls_namespace='eventapi')

@eve.post("/events/", response=EventSchema)
def create_event(request, payload: EventSchema):
    event = Event.objects.create(**payload.dict())
    return event

@eve.get("/events/", response=List[EventSchema])
def list_events(request):
    events = Event.objects.all()
    return events

@eve.get("/events/{event_id}", response=EventSchema)
def get_event(request, event_id: int):
    event =  Event.objects.get(event_id=event_id)
    return event

@eve.put("/events/{event_id}/", response=EventSchema)
def update_event(request, event_id: int, payload: EventSchema):
    event = Event.objects.get(event_id=event_id)
    for attr, value in payload.dict().items():
        setattr(event, attr, value)
    event.save()
    return event

@eve.delete("/events/{event_id}/")
def delete_event(request, event_id: int):
    event = Event.objects.get(event_id=event_id)
    event.delete()
    return {"success": True}
