from django.http import JsonResponse
import json
from ..models import User_Adress, User_Payment_Card
from django.views.decorators.csrf import csrf_exempt

def checkout(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            card_number = body.get('card_number')
            card_titular_name = body.get('card_titular_name')
            card_cvc = body.get('card_cvc')
            card_expiration = body.get('card_expiration')
            card_method = body.get('card_method')
            adress_street = body.get('adress_street')
            adress_number = body.get('adress_street')
            adress_complement= body.get('adress_street')
            adress_district = body.get('adress_street')
            adress_state = body.get('adress_street')
            adress_city = body.get('adress_city')
            user_session = request.session.session_key

            adress = User_Adress.objects.create(
                  street=adress_street,
                    number=adress_number,
                    complement=adress_complement,
                    district=adress_district,
                    state=adress_state,
                    city=adress_city,
                    user_session=user_session
            )

            card = User_Payment_Card.objects.create(
                number=card_number,
                titular_name=card_titular_name,
                cvc=card_cvc,
                expiration_date=card_expiration,
                method=card_method,
                user_session = user_session
            )

            return JsonResponse({'message': 'Checkout realizado com sucesso'}, status=200)








        except Exception as e:
            print(f"Erro ao realizar checkout: {e}")
            return JsonResponse({'error': 'Erro ao realizar checkout'}, status=500)