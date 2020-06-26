from django.shortcuts import render, HttpResponse, redirect

from host import models
from utils import pagination

# Create your views here.


def data(request):
    if request.method == "GET":
        # models.Bussiness.objects.create(caption='DBA', code='dba')
        # models.Bussiness.objects.create(caption='CACHE', code='cache')
        # models.Bussiness.objects.create(caption='SQL', code='sql')
        # models.Bussiness.objects.create(caption='DB', code='db')
        # models.Bussiness.objects.create(caption='PYTHON', code='python')
        # models.Application.objects.create(name='qq')
        # models.Application.objects.create(name='wechat')
        # models.Application.objects.create(name='scdn')
        # models.Application.objects.create(name='facebook')
        # models.Application.objects.create(name='lol')
        # for x in range(500):
        #     n = "test" + str(x)
        #     models.Application.objects.create(name=n)

        # models.Host.objects.create(hostname="c1",ip="10.0.0.1",port=8001,b_id=1)
        # models.Host.objects.create(hostname="c2", ip="10.0.0.2", port=8002, b_id=2)
        # models.Host.objects.create(hostname="c3", ip="10.0.0.3", port=8003, b_id=3)
        # models.Host.objects.create(hostname="c4", ip="10.0.0.4", port=8004, b_id=4)
        # models.Host.objects.create(hostname="c5", ip="10.0.0.5", port=8005, b_id=2)
        # models.Host.objects.create(hostname="c6", ip="10.0.0.6", port=8006, b_id=3)
        # models.Host.objects.create(hostname="c7", ip="10.0.0.7", port=8007, b_id=4)
        # models.Host.objects.create(hostname="c8", ip="10.0.0.8", port=8008, b_id=5)

        # obj = models.Application.objects.filter(id=1).first()
        # obj.r.add(1,2,3)
        # obj = models.Application.objects.filter(id = 2).first()
        # obj.r.add(4, 2, 3)
        # obj = models.Application.objects.filter(id = 3).first()
        # obj.r.add(1, 4, 5)
        # obj = models.Application.objects.filter(id= 4).first()
        # obj.r.add(3, 5, 6)
        # obj = models.Application.objects.filter(id= 5).first()
        # obj.r.add(4, 5, 7)
        return HttpResponse('ok')
    elif request.method == "POST":
        pass


def application(request):
    if request.method == "GET":
        applications = models.Application.objects.all()
        total_count = len(applications)
        current_page = int(request.GET.get('p', 1))
        per_page_count = request.COOKIES.get('per_page_count')
        print('per_page_count', per_page_count)
        print(current_page)
        print(len(applications))
        app_obj = pagination.Page(current_page, total_count, int(per_page_count))
        applications = applications[int(app_obj.start):int(app_obj.end)]
        return render(request, "application.html", {'apps': applications, "page_str": app_obj.page_str()})
    elif request.method == "POST":
        pass


def del_app(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        id = request.POST.get('app_id')
        print(id)
        models.Application.objects.filter(id=id).delete()
        return redirect('/application/')


def edit_app(request, p):
    if request.method == "POST":
        aid = request.POST.get('id')
        name = request.POST.get('app_name')
        hosts = request.POST.getlist('host')
        print('hello', hosts, type(hosts))
        models.Application.objects.filter(id=aid).update(name=name)
        obj = models.Application.objects.filter(id=aid).first()
        obj.r.set(hosts)
        return redirect('/application/')
    elif request.method == "GET":
        print(p)
        app_data = models.Application.objects.filter(id=p).first()
        hosts = models.Host.objects.all()
        return render(request, "edit_app.html", {"app_data": app_data, "hosts": hosts})


def add_app(request):
    if request.method == "POST":
        name = request.POST.get('add_app')
        models.Application.objects.create(name=name)
        return redirect("/application/")
    elif request.method == "GET":
        return render(request, "add_app.html")


def bussiness(request):
    if request.method == "GET":
        bussiness = models.Bussiness.objects.all()
        hosts = models.Bussiness.objects.filter(id=2).first().hosts.all()
        for host in hosts:
            print(host.hostname)
        return render(request, "bussiness.html", {'bussiness': bussiness})
    elif request.method == "POST":
        pass


def add_buss(request):
    if request.method == "GET":
        return render(request, "add_buss.html")
    elif request.method == "POST":
        caption = request.POST.get('caption')
        code = request.POST.get("code")
        models.Bussiness.objects.create(caption=caption, code=code)
        return redirect("/bussiness/")


def edit_buss(request, bid):
    if request.method =='GET':
        print(bid)
        buss = models.Bussiness.objects.filter(id=bid).first()
        return render(request, "edit_buss.html", {"buss": buss})
    elif request.method == 'POST':
        bid = request.POST.get('bid')
        caption = request.POST.get('caption')
        code = request.POST.get('code')
        models.Bussiness.objects.filter(id=bid).update(caption=caption, code=code)
        return redirect("/bussiness/")


def del_buss(request):
    if request.method =='GET':
        pass
    elif request.method == 'POST':
        bid = request.POST.get("bid")
        models.Bussiness.objects.filter(id=bid).delete()
        return redirect('/bussiness/')


def auth(func):
    def inner(request, *args, **kwargs):
        username = request.COOKIES.get("username")
        print("host", username)
        if not username:
            return redirect("/login/")
        return func(request, *args, **kwargs)
    return inner

@auth
def host(request):
    if request.method == "GET":
        # username = request.COOKIES.get("username")
        # print("host", username)
        # if not username:
        #     return redirect("/login/")
        hosts = models.Host.objects.all()
        buss = models.Bussiness.objects.all()
        return render(request, "host.html", {'hosts': hosts, "buss": buss})
    elif request.method =="POST":
        pass


def edit_host(request, hid):
    if request.method == "GET":
        host = models.Host.objects.filter(hid=hid).first()
        buss = models.Bussiness.objects.all()
        return render(request, "edit_host.html", {"host": host, 'buss': buss})
    elif request.method == "POST":
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        b_id = request.POST.get('buss')
        models.Host.objects.filter(hid=hid).update(hostname=hostname, ip=ip, port=port, b_id=b_id)
        return redirect("/host/")


user = {"seth":{"pwd": "123"}}

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        dic = user.get(u)
        print("dic", dic)
        if not dic:
            print("wrong")
            return redirect("/login/")
        elif p == dic["pwd"]:
            print("right")
            res = redirect("/host/")
            res.set_cookie("username", u)
            return res
        else:
            print("wrong")
            return redirect("/login/")