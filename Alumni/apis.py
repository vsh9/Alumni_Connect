from ninja import NinjaAPI
from .models import Alumni
from .schema import AlumniSchema
from typing import List

app = NinjaAPI()
 
@app.get("/alumni", response=List[AlumniSchema])
def list_alumni(request):
    return list(Alumni.objects.all())

@app.post("/alumni", response=AlumniSchema)
def create_alumni(request, payload: AlumniSchema):
    alumni = Alumni.objects.create(**payload.dict())
    return alumni

@app.get("/alumni/{alumni_id}", response=AlumniSchema)
def get_alumni(request, alumni_id: int):
    alumni = Alumni.objects.get(pk=alumni_id)
    return alumni

@app.put("/alumni/{alumni_id}", response=AlumniSchema)
def update_alumni(request, alumni_id: int, payload: AlumniSchema):
    alumni = Alumni.objects.get(pk=alumni_id)
    for attr, value in payload.dict().items():
        setattr(alumni, attr, value)
    alumni.save()
    return alumni

@app.delete("/alumni/{alumni_id}", response=dict)
def delete_alumni(request, alumni_id: int):
    alumni = Alumni.objects.get(pk=alumni_id)
    alumni.delete()
    return {"success": True}
