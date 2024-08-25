import json
from Alumni.models import alumni  
from .models import Event

def load_json_data(filename='sample_event_data.json'):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    
    event_objects = []
    for item in data:
        event = Event(
            event_name=item['event_name'],
            event_date=item['event_date_time'],
            location=item['location'],
            description=item['description'],
            event_type=item['event_type'],
            registration_deadline=item['registration_deadline'],
            rsvp_deadline=item['rsvp_deadline'],
            speaker_details=item.get('speaker_details', ''),
            event_status=item['event_status'],
            feedback_available=item.get('feedback_available', False)
        )
        event_objects.append(event)
        
    Event.objects.bulk_create(event_objects)

if __name__ == "__main__":
    load_json_data()