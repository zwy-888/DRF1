from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from app1.models import User

app_name = "A"


# django视图模式分为两种
# 函数视图 FBV function base view
# 类视图 CBV class base view
# @csrf_protect 为某个函数单独开启csrf认证
@csrf_exempt  # 为函数免于csrf认证
def a(request):
    if request.method == "GET":
        print(request.GET.get("name"))
        return JsonResponse({"state": 'get_ok'})
    if request.method == "POST":
        print(request.POST.get("name"))
        return JsonResponse({"state": 'post_ok'})


@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self, request, *args, **kwargs):
        print('get  查询')
        return HttpResponse("get 成功")

    def post(self, request, *args, **kwargs):
        print('post  新增')
        return HttpResponse("pos 成功")

    # def get(self, request, *args, **kwargs):
    #     print('get  查询')
    #     return HttpResponse("get 成功")

    def delete(self, request, *args, **kwargs):
        print('delete 删除')
        return HttpResponse("delete 成功")


@method_decorator(csrf_exempt, name="dispatch")
class Api(View):
    def get(self, request, *args, **kwargs):
        # request.Get.get(id)

        user_id = kwargs.get("id")
        if user_id:
            # print(user_id)
            user_obj = User.objects.filter(id=user_id).values().first()
            # .values()后得到的是数据是<QuerySet，然后.first()得到的是字典
            # print(user_obj, type(user_obj))
            if user_obj:
                return JsonResponse({
                    "status": 200,
                    "msg": "单个用户查询",
                    "rst": user_obj})
        else:
            user_all = User.objects.all().values()
            print(user_all, type(user_all))
            print(list(user_all))
            return JsonResponse({
                "status": 200,
                "msg": "查询所有",
                "rst": list(user_all),
            })
        return JsonResponse({
            "status": 500,
            "msg": "用户不存在"})

    def post(self, request, *args, **kwargs):
        # request.POST.get()
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")

        try:
            user_obj = User.objects.create(username=username, password=pwd, email=email)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "email": user_obj.email}
            })

        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class UserAPIView(APIView):

    # def get(self, request, *args, **kwargs):
    #     print("这是drf的get请求")
    #     a = request._request.GET.get("name")
    #     b = request.GET.get("name")
    #     print(request.query_params)
    #     print(request.data)
    #     print(a)
    #     return Response("DRF GET OK")
    #
    # def post(self, request, *args, **kwargs):
    #     print("这是drf的post请求")
    #     return Response("DRF POST OK")

    def get(self, request, *args, **kwargs):
        print("这是drf的get请求")
        request.GET.get("name")
        # return Response("haha1")
        # user_id = kwargs.get("id")  #"detail": "Method \"GET\" not allowed."
        user_id = request.GET.get("id")
        print(user_id)
        print(request.query_params, "aaa")
        print(request.data, "bbb")
        # user_id = request.data
        # print(request.data)
        if user_id:
            # print(user_id)
            user_obj = User.objects.filter(id=user_id).values().first()
            # .values()后得到的是数据是<QuerySet，然后.first()得到的是字典
            # print(user_obj, type(user_obj))
            if user_obj:
                return Response({
                    "status": 200,
                    "msg": "rsf单个用户查询",
                    "rst": user_obj})
        else:
            user_all = User.objects.all().values()
            print(user_all, type(user_all))
            print(list(user_all))
            return Response({
                "status": 200,
                "msg": "查询所有",
                "rst": list(user_all),
            })
        return Response({
            "status": 500,
            "msg": "用户不存在"})

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")
        print(request.query_params, "111")
        print(request.data, "222")
        try:
            user_obj = User.objects.create(username=username, password=pwd, email=email)
            return Response({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "email": user_obj.email}
            })

        except:
            return Response({
                "status": 500,
                "message": "创建用户失败",
            })

    def put(self, request, *args, **kwargs):
        user_obj = request.query_params
        id = user_obj["id"]
        username = user_obj["username"]  # 获取QueryDict里面东西的方法
        pwd = user_obj.get("pwd")
        email = user_obj.get("email")
        print(username, pwd, email, id)
        a = User.objects.filter(id=id).first()
        print(type(a))
        a.username = username
        a.password = pwd
        # a.gender =
        a.email = email
        a.save()
        print(a)

        # print(request.query_params, "ccc")
        # print(request.data, "ddd")  # 获取不到
        # email = request.PUT.get("email") 也获取不到
        return Response({"status": 200,
                         "message": 'ok',
                         "rst": a.username})
