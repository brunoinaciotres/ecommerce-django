from django.http import HttpResponse, JsonResponse
import json
from ..models import Product, OrderItem
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            product = Product.objects.get(id=product_id)
            order_item, created = OrderItem.objects.get_or_create(
                product=product,
                status='aberto',
                defaults={'product_amount': 1}
            )
            
            if not created:
                order_item.product_amount += 1
                print("aqui")
            order_item.save()
        
            # Inicializa a sessão 'order_items' se não existir
            if 'order_items' not in request.session:
                request.session['order_items'] = []
            
            item_already_in_session = False

            # Verifica se o item já está na sessão e atualiza a quantidade
            for item in request.session['order_items']:
                if order_item.id == item['order_item_id']:
                    item['product_amount'] = order_item.product_amount
                    item_already_in_session = True
                    break

            # Se o item não estiver na sessão, adiciona um novo
            if not item_already_in_session:       
                request.session['order_items'].append({
                    "order_item_id": order_item.id,
                    "product_amount": order_item.product_amount
                })
            
            # Calcula a quantidade total de itens no carrinho
            total_items_count = sum(item['product_amount'] for item in request.session['order_items'])
            request.session['total_items_count'] = total_items_count

            # Marca a sessão como modificada para garantir que seja salva
            request.session.modified = True
            
            return JsonResponse({
                'message': 'Produto adicionado ao carrinho',
                'order_items': request.session['order_items'],
                'total_items_count': request.session['total_items_count']
            }, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
        except Exception as e:
            print(f"Erro ao adicionar ao carrinho: {e}")
            return JsonResponse({'error': 'Erro ao adicionar ao carrinho'}, status=500)