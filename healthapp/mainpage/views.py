from django.shortcuts import render

# Create your views here.

#-----------New Example-----------

from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import UserSerializer


class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer










# -------- In class code -------------
# from .models import User
# from .forms import UserForm
# from django.http import JsonResponse
# from django.views import View
# from .models import User
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from django.contrib import auth
# import json


# def user_list(request):
#   users = User.objects.all()
#   return render(request, 'mainpage/user_list.html', {'users': users})

# # user Show
# def user_detail(request, pk):
#   user = User.objects.get(id=pk)
#   return render(request, 'mainpage/user_detail.html', {'user': user})

# # user Create
# def user_create(request):
#   if request.method == 'POST':
#     form = UserForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       return redirect('user_detail', pk=user.pk)
#   else:
#     form = UserForm()
#   return render(request, 'mainpage/user_form.html', {'form': form})

# # user Edit
# def user_edit(request, pk):
#   user = User.objects.get(pk=pk)
#   if request.method == 'POST':
#     form = UserForm(request.POST, instance=user)
#     if form.is_valid():
#       user = form.save()
#       return redirect('user_detail', pk=user.pk)
#   else:
#     form = UserForm(instance=user)
#   return render(request, 'mainpage/user_form.html', {'form': form})

# # user Delete
# def user_delete(request, pk):
#   User.objects.get(id=pk).delete()
#   return redirect('user_list')









# -----------------Original Code --------------------


# class CreateUser(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(CreateUser, self).dispatch(request, *args, **kwargs)
    
#     def post(self, request):
#         data = request.body.decode('utf-8')
#         data = json.loads(data)
#         try: 
#             new_user = User(username=data["username"], password=data["password"])
#             new_user.set_password(new_user.password)
#             new_user.save()
#             return JsonResponse({"created": data}, safe=False)
#         except:
#             return JsonResponse({"error": "Data is Not Valid"}, safe=False)

# class Users(View):
# # Create your views here.
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(Users, self).dispatch(request, *args, **kwargs)

#     def get(self, request):
#         User_list = list(Users.objects.values())
#         return JsonResponse({
#         'Content-Type': 'application/json',
#         'status': 200,
#         'data': User_list
#         }, safe=False)
    
#     def post(self, request):
#         data = request.body.decode('utf-8')
#         print(data)
#         data = json.loads(data)
#         try:
#             new_User = User(name=data["name"], weight=data["weight"], water=data["water"], alcohol=data["alcohol"], caffeine=data["caffeine"] )
        
#             new_User.save()
#             print('this is a new User', new_User.id)
#             return JsonResponse({"created": data}, safe=False)
#         except:
#             return JsonResponse({"error": "not valid data"}, safe=False)
    
    
# class User_detail(View):
    
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(Users, self).dispatch(request, *args, **kwargs)


#     def get(self, request, pk):
#         User_list = list(Users.objects.filter(pk=pk).values())
#         return JsonResponse({"data": User_list}, safe=False)
    
#     def post(self, request):
#         data: request.decode.body('utf-8')
#         print(data)
#         data=json.loads(data)
    
#         try: 
#             edit_User = Users.objects.get(pk=pk)
#             data_key = list(data.keys())
#             for key in data_key:
#                 if key == "name":
#                     edit_User.name = data[key]
#                 if key == "weight":
#                     edit_User.weight = data[key]
#                 if key == "water":
#                     edit_User.water = data[key]
#                 if key == 'alcohol':
#                     edit_User.alcohol = data[key]
#                 if key == 'caffeine':
#                     edit_User.caffeine =data[key]
                

#             edit_User.save()
#             return JsonResponse({"updated":data},  safe=False)
#         except User.DoesNotExist:
#             return JsonResponse({"User does not exist"})
    
#     def delete(self, requests, pk):
#         try: 
#             User_delete = Users.objects.get(pk=pk)
#             User_delete.delete()
#             return JsonResponse({"Deleted": True}, safe = False)
#         except:
#             return JsonResponse({"error": "Not a valid key"}, safe= False)

# class Authentication(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(Authentication, self).dispatch(request, *args, **kwargs)

#     def post(self, request):
#         data = request.body.decode('utf-8')
#         data = json.loads(data)
#         user = auth.authenticate(username=data["username"], password=data["password"])
#         if user is not None:
#             auth.login(request, user)
#             return JsonResponse({"response": "login successful", "data": data}, safe=False)
#         else: 
#             return JsonResponse({"response": "login unseccessful", "data": data},safe=False)

# @csrf_exempt
# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return JsonResponse({"response": "logout successful"},safe=False)