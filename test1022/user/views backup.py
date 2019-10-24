import json
import jwt
import bcrypt                  

import datetime
from django.views import View
from django.http  import JsonResponse,HttpResponse 
from .models      import Users


class AccountView(View):
    def post(self, request):
        # 여기서 암호화
        data = json.loads(request.body)
        print(data)
        bytedPw = bytes(data["password"],"utf-8")
        print(bytedPw)
        print(type(bytedPw))
        hashPw = bcrypt.hashpw(bytedPw, bcrypt.gensalt())
        print(hashPw)
        print(type(hashPw))
        decodedPw = hashPw.decode('utf-8')
        print(decodedPw)
        print(type(decodedPw))
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
       # json을 딕셔너리로        
        data = json.loads(request.body)
        try:
            user=Users.objects.get(email=data['email'])
            encoded_jwt_email = jwt.encode({'email':user.email},user.email,algorithm='HS256' )
            
            # print(data)
            # print(data['email'])
            # print(user.password)
            # print(user.id)
            # print(user.email)
            # print(type(user))
            # elif user.name != data['name']:
            #     return JsonResponse({"message":"NOT_MATCHED_ID"},status=400)
            if bcrypt.checkpw(data['password'].encode("UTF-8"), user.password.encode("UTF-8")):
                return JsonResponse(
                            {
                                "access_token" : encoded_jwt_email.decode("UTF-8"),
                            }
                        )
            else:
                return JsonResponse({'message' : '비밀번호를 다시 확인해주세요.'}, status=400)
            
            # if user.password != data['password']:
            #     return JsonResponse({"message":"INVALID_PASSWORD"},status=401)
            return JsonResponse({"message":"SUCCESS"},status=200)
        except Users.DoesNotExist:
            return JsonResponse({"message":"INVALID_USER"}, status=401)
        except Exception as e:
            print(e)
            return HttpResponse(status=500)

        
        # try:
        #     user=Users.objects.get(email=data['email'])
        #     if user.name == data['name']:
        #         return JsonResponse("message: No_ID",status=401)
        #     elif user.password == False:
        #         return JsonResponse("message: No_PW",status=401)
        #     if user.name != data['name']:
        #         return JsonResponse("message: INVALID_ID",status=403)
        #     elif user.password != data['password']:
        #         return JsonResponse({"message":"INVALID_PASSWORD"},status=401)
        #     return JsonResponse({"message":"SUCCESS"},status=200)
        # except Users.DoesNotExist:
        #     return JsonResponse({"message":"INVALID_USER"}, status=401)
# class Au