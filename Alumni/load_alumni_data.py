import json
from Alumni.models import alumni
def load_json_data(filename='sample_alumni_data.json', batch_size=500):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    
    alumni_objects = []
    for item in data:
        al = alumni(
            name=item['name'],
            email=item['email'],
            graduation_year=item['graduation_year'],
            phone=item['phone'],
            address=item['address'],
            occupation=item['occupation'],
            company=item['company'],
            linkedIn_profile=['linkedIn_profile'],
            bio=['bio']
        )
        alumni_objects.append(al)
        
        # Insert records in batches
        if len(alumni_objects) >= batch_size:
            alumni.objects.bulk_create(alumni_objects)
            alumni_objects = []  # Clear the list after inserting

    # Insert any remaining objects that didn't make up a full batch
    if alumni_objects:
        alumni.objects.bulk_create(alumni_objects)

if __name__ == "__main__":
    load_json_data()
