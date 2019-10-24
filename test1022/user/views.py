import json
from django.views import View
from django.http  import JsonResponse 
from .models      import Users


class AccountView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        Users.objects.create(
            name     = data["name"],
            password = data["password"],
            email    = data["email"]
        ).save()
        return JsonResponse({"message":"SUCCESS"}, status=200)
    def get(self, request):
        userinfo = list(Users.objects.values())
        return JsonResponse({"data":userinfo},status=200)
class AuthView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            user=Users.objects.get(email=data['email'])
            if user.name != None:
                return JsonResponse("message: No_ID",status=401)
            elif user.password != None:
                return JsonResponse("message: No_PW",status=401)
            elif user.name != data['name']:
                return JsonResponse("message: INVALID_ID",status=401)
            elif user.password != data['password']:
                return JsonResponse({"message":"INVALID_PASSWORD"},status=401)
            return JsonResponse({"message":"SUCCESS"},status=200)
        except Users.DoesNotExist:
            return JsonResponse({"message":"INVALID_USER"}, status=401)
# class Au