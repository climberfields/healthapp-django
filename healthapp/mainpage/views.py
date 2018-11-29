from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class Users(View):
# Create your views here.
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Users, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        User_list = list(User.objects.values())
        return JsonResponse({
        'Content-Type': 'application/json',
        'status': 200,
        'data': User_list
        }, safe=False)
    
    def post(self, request):
        data = request.body.decode('utf-8')
        print(data)
        data = json.loads(data)
        try:
            new_User = User(name=data["name"], water=data["water"], alcohol=data["alcohol"], caffeine=data["caffeine"] )
        
            new_User.save()
            print('this is a new User', new_User.id)
            return JsonResponse({"created": data}, safe=False)
        except:
            return JsonResponse({"error": "not valid data"}, safe=False)
    
    
class User_detail(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(User, self).dispatch(request, *args, **kwargs)


    def get(self, request, pk):
        User_list = list(User.objects.filter(pk=pk).values())
        return JsonResponse({"data": User_list}, safe=False)
    
    def post(self, request):
        data: request.decode.body('utf-8')
        print(data)
        data=json.loads(data)
    
        try: 
            edit_User = User.objects.get(pk=pk)
            data_key = list(data.keys())
            for key in data_key:
                if key == "name":
                    edit_User.name = data[key]
                if key == "water":
                    edit_User.water = data[key]
                if key == "alcohol":
                    edit_User.alcohol = data[key]
                if key == 'caffeine':
                    edit_User.caffeine = data[key]
                if key == 'weight':
                    edit_User.weight =data[key]
                if key == 'age':
                    edit_User.age = data[key]

            edit_User.save()
            return JsonResponse({"updated":data},  safe=False)
        except User.DoesNotExist:
            return JsonResponse({"User does not exist"})
    
    def delete(self, requests, pk):
        try: 
            User_delete = User.objects.get(pk=pk)
            User_delete.delete()
            return JsonResponse({"Deleted": True}, safe = False)
        except:
            return JsonResponse({"error": "Not a valid key"}, safe= False)