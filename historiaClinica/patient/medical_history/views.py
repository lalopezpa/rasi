from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_PUT
from django.db.models import F

from .models import MedicalHistoryEntity

@require_GET
def get_medical_history(request, id):
    medical_history_entity = MedicalHistoryEntity.objects.get(id=id)
    medical_history = {
        'id': medical_history_entity.id,
        'medical_history': medical_history_entity.medical_history,
        'hash': medical_history_entity.hash,
    }

    # Realiza la verificación del hash aquí si es necesario

    return JsonResponse(medical_history)

@require_PUT
def update_medical_history(request, id):
    # Obtén los datos del cuerpo de la solicitud
    medical_history_text = request.POST.get('text', '')

    # Realiza la actualización del modelo según tus necesidades
    medical_history_entity = MedicalHistoryEntity.objects.get(id=id)
    medical_history_entity.text = medical_history_text
    medical_history_entity.hash = sha256(medical_history_text.encode()).hexdigest()
    medical_history_entity.save()

    return JsonResponse({
        'id': medical_history_entity.id,
        'text': medical_history_entity.text,
        'hash': medical_history_entity.hash,
    })
