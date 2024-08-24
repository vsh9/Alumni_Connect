from ninja import NinjaAPI
from .models import ML
from django.shortcuts import get_object_or_404
from .schemas import MLCreateSchema, MLReadSchema
from Notifications.models import Notification

router = NinjaAPI(urls_namespace='mlapi')

#To create message log
@router.post('/ml/', response=MLReadSchema)
def create_ml(request, data: MLCreateSchema):
    ntf = Notification.objects.create(n_id=data.n_id)
    ml = ML.objects.create(
        n_id=ntf,
        alumni_id=data.alumni_id,
        message = data.message,
        sent_at = data.sent_at,
        response=data.response_status
    )
    return ml

#To get message log
@router.get('/ml/{ml_id}', response=MLReadSchema)
def get_ml(request, ml_id: int):
    ml = ML.objects.get(ML, ml_id=ml_id)
    return ml

#To list all the the message logs
@router.get('/ml/', response=list[MLReadSchema])
def list_ml(request):
    ml_list = ML.objects.all()
    return ml_list

#To update the message log
@router.put('/ml/{ml_id}', response=MLReadSchema)
def update_ml(request, ml_id: int, data: MLCreateSchema):
    ml = get_object_or_404(ML, ml_id=ml_id)
    for attr, value in data.dict().items():
        setattr(ml, attr, value)
    setattr(ml,'ml_id',ml_id)
    ml.save()
    return ml

#To delete the message log
@router.delete('/ml/{ml_id}', response={204: None})
def delete_ml(request, ml_id: int):
    ml = get_object_or_404(ML, ml_id=ml_id)
    ml.delete()
    return 204, None
