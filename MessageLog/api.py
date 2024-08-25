from ninja import NinjaAPI
from .models import ML
from django.shortcuts import get_object_or_404
from .schemas import MLCreateSchema, MLReadSchema
from Notifications.models import Notification
from Alumni.models import alumni
import json

router = NinjaAPI(urls_namespace='mlapi')

#To create message log
@router.post('/ml/', response=MLReadSchema)
def create_ml(request, data: MLCreateSchema):
    ntf = Notification.objects.get(n_id=data.n_id)
    al = alumni.objects.get(phone_number= data.phone_no)
    data.message = ntf.n_content
    ml = ML.objects.create(
        n_id=ntf,
        p_no=al,
        message = data.message,
        sent_at = data.sent_at,
        response_status=data.response_status
    )
    return {
        "ml_id": ml.ml_id,
        "n_id": ml.n_id.n_id,
        "phone_no": ml.p_no.phone_number,
        "message": ml.message,
        "sent_at": ml.sent_at.isoformat(),
        "delivery_status": ml.delivery_status,
        "response_status": ml.response_status
    }

#To get message log
@router.get('/ml/{ml_id}', response=MLReadSchema)
def get_ml(request, ml_id: int):
    ml = ML.objects.get(ml_id=ml_id)
    return {
        "ml_id": ml.ml_id,
        "n_id": ml.n_id.n_id,
        "phone_no": ml.p_no.phone_number,
        "message": ml.message,
        "sent_at": ml.sent_at.isoformat(),
        "delivery_status": ml.delivery_status,
        "response_status": ml.response_status
    }

#To list all the the message logs
@router.get('/ml/', response=list[MLReadSchema])
def list_ml(request):
    ml_list = ML.objects.all()
    response_list = []
    for ml in ml_list:
        ml_list2 = {
            "ml_id": ml.ml_id,
            "n_id": ml.n_id.n_id,
            "phone_no": ml.p_no.phone_number,
            "message": ml.message,
            "sent_at": ml.sent_at.isoformat(),
            "delivery_status": ml.delivery_status,
            "response_status": ml.response_status
        }
        response_list.append(MLReadSchema(**ml_list2))
    return response_list

#To update the message log
@router.put('/ml/{ml_id}', response=MLReadSchema)
def update_ml(request, ml_id: int, data: MLCreateSchema):
    ml = get_object_or_404(ML, ml_id=ml_id)
    ntf = get_object_or_404(Notification, n_id=data.n_id)
    al = get_object_or_404(alumni, phone_number=data.phone_no)
    data.n_id = ntf
    data.phone_no = al
    data.message = ntf.n_content
    for attr, value in data.dict().items():
        setattr(ml, attr, value)
    setattr(ml,'ml_id',ml_id)
    ml.save()
    return {
        "ml_id": ml.ml_id,
        "n_id": ml.n_id.n_id,
        "phone_no": ml.p_no.phone_number,
        "message": ml.message,
        "sent_at": ml.sent_at.isoformat(),
        "delivery_status": ml.delivery_status,
        "response_status": ml.response_status
    }

#To delete the message log
@router.delete('/ml/{ml_id}', response= dict)
def delete_ml(request, ml_id: int):
    ml = get_object_or_404(ML, ml_id=ml_id)
    ml.delete()
    return  {"done": "success"}
