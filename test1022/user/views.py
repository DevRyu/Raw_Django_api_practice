import json
import jwt
import bcrypt                  

import datetime
from django.views import View
from django.http  import JsonResponse,HttpResponse 
from .models      import Users


class AccountView(View):

    def post(self, request):
        data = json.loads(request.body)
        bytedPw = bytes(data["password"],"utf-8")
        hashPw = bcrypt.hashpw(bytedPw, bcrypt.gensalt())
        decodedPw = hashPw.decode('utf-8')
        Users.objects.create(
            name     = data["name"],
            password = decodedPw,
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
            encoded_jwt_email = jwt.encode({'email':user.email},user.email,algorithm='HS256' )
            if bcrypt.checkpw(data['password'].encode("UTF-8"), user.password.encode("UTF-8")):
                return JsonResponse({"access_token" : encoded_jwt_email.decode("UTF-8"),})
            else:
                return JsonResponse({'message' : '비밀번호 틀렸다 인간'}, status=400)
            return JsonResponse({"message":"SUCCESS"},status=200)

        except Users.DoesNotExist:
            return JsonResponse({"message":"INVALID_USER"}, status=401)

        except Exception as e:
            print(e)
            return HttpResponse(status=500)

# class Au