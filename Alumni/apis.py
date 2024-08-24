from ninja import NinjaAPI
from .models import alumni
from .schema import AlumniSchema
from typing import List

app = NinjaAPI()
 
@app.get("/alumni", response=List[AlumniSchema])
def list_alumni(request):
    return list(alumni.objects.all())

@app.post("/alumni", response=AlumniSchema)
def create_alumni(request, payload: AlumniSchema):
    al = alumni.objects.create(**payload.dict())
    return al

@app.get("/alumni/{alumni_id}", response=AlumniSchema)
def get_alumni(request, alumni_id: int):
    al = alumni.objects.get(pk=alumni_id)
    return al

@app.put("/alumni/{alumni_id}", response=AlumniSchema)
def update_alumni(request, alumni_id: int, payload: AlumniSchema):
    al = alumni.objects.get(pk=alumni_id)
    for attr, value in payload.dict().items():
        setattr(al, attr, value)
    al.save()
    return al

@app.delete("/alumni/{alumni_id}", response=dict)
def delete_alumni(request, alumni_id: int):
    al = alumni.objects.get(pk=alumni_id)
    al.delete()
    return {"success": True}
