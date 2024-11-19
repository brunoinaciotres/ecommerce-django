from django.http import JsonResponse
import json
from ..models import OrderItem
from django.views.decorators.csrf import csrf_exempt

def checkout(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
        except Exception as e:
            print(f"Erro ao realizar checkout: {e}")
            return JsonResponse({'error': 'Erro ao realizar checkout'}, status=500)