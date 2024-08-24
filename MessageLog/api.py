from ninja import Router
from .models import ML
from django.shortcuts import get_object_or_404
from .schemas import MLCreateSchema, MLReadSchema

router = Router()

@router.post('/ml/', response={201: MLReadSchema})
def create_ml(request, data: MLCreateSchema):
    ml = ML.objects.create(**data.dict())
    return 201, ml

@router.get('/ml/{ml_id}', response=MLReadSchema)
def get_ml(request, ml_id: int):
    ml = get_object_or_404(ML, ml_id=ml_id)
    return ml

@router.get('/ml/', response=list[MLReadSchema])
def list_ml(request):
    ml_list = ML.objects.all()
    return ml_list

@router.put('/ml/{ml_id}', response=MLReadSchema)
def update_ml(request, ml_id: int, data: MLCreateSchema):
    ml = get_object_or_404(ML, ml_id=ml_id)
    for attr, value in data.dict().items():
        setattr(ml, attr, value)
    ml.save()
    return ml

@router.delete('/ml/{ml_id}', response={204: None})
def delete_ml(request, ml_id: int):
    ml = get_object_or_404(ML, ml_id=ml_id)
    ml.delete()
    return 204, None
