from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_user_session(request):
    if request.method == "GET":
        session_id = request.session.session_key
        if session_id is None:
            request.session.create()
            session_id = request.session.session_key
        
        return JsonResponse({"session_id": session_id})
            