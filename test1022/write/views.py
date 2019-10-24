import json
from django.views import View
from django.http  import JsonResponse
from .models      import WriteTable
    
class Write(View):
    def get(self, resquest):
        friend_list = list(WriteTable.objects.values())
        return JsonResponse(friend_list, safe=False) 


class WriteDetail(View):