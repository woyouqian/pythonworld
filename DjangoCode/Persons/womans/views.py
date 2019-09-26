from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from womans.models import Money
from time import localtime, asctime

# Create your views here.


def index(request):
    return render_to_response('index.html')


def womans(request):
    return render_to_response('women.html')


def add_money(request):
    return render(request, 'add_money.html')


def create_money(request):
    date = asctime(localtime())
    name = request.GET['name']
    number = request.GET['number']
    charge = request.GET['charge']
    buy = request.GET['buy']
    _mark = request.GET['mark']
    mark = date+' : '+_mark

    money = Money()
    money.name = name
    money.number = number
    money.charge = charge
    money.buy = buy
    money.mark = mark
    money.save()

    # return HttpResponse("This data has been saved ok! Thanks.")
    return get_all_money(request)


def get_all_money(request):
    error = True
    all_money = Money.objects.all()
    if not all_money:
        error = False
    return render_to_response('all_money.html', {'all_money': all_money, 'error': error})


def search_money(request):
    error = True
    return render_to_response('search_money.html', {'error': error})


def get_one_detail(request):
    name = request.GET['name']
    sb_money = Money.objects.filter(name=name)
    if sb_money:
        sum_charge, sum_buy, count = sum_count(sb_money)
        return render_to_response('detail.html', {'sb_money': sb_money,
                                                  'charge': sum_charge, 'buy': sum_buy, 'count': count})
    else:
        error = False
        return render_to_response('search_money.html', {'error': error, 'name': name})


def get_all_number(request):
    error = True
    all_money = Money.objects.all()
    if not all_money:
        error = False
    return render_to_response('operate_money.html', {'all_money': all_money, 'error': error})


def delete_money(request):
    _id = request.GET['delete']
    Money.objects.get(id=int(_id)).delete()
    return get_all_money(request)


def get_one_money(request):
    _id = request.GET['editor']
    money = Money.objects.get(id=int(_id))
    return render(request, 'update_money.html', {'money': money})


def update_money(request):
    date = asctime(localtime())
    _id = request.GET['id']
    money = Money.objects.get(id=int(_id))

    charge = request.GET['charge']
    buy = request.GET['buy']
    _mark = request.GET['mark']
    mark = date + ' : ' + _mark

    money.charge = charge
    money.buy = buy
    money.mark = mark
    money.save()

    return get_all_money(request)


def charge_money(request):
    return render(request, 'charge_money.html')


def charge_one_money(request):
    name = request.GET['name']
    number = request.GET['number']

    date = asctime(localtime())
    charge = request.GET['charge']
    _mark = request.GET['mark']
    mark = date + ' : ' + _mark

    money = Money()
    money.name = name
    money.number = number
    money.charge = charge
    money.buy = 0
    money.mark = mark
    money.save()

    return get_all_money(request)


def buy_money(request):
    return render(request, 'buy_money.html')


def buy_one_money(request):
    name = request.GET['name']
    number = request.GET['number']
    sb_money = Money.objects.filter(name=name)
    sum_charge, sum_buy, count = sum_count(sb_money)

    date = asctime(localtime())
    buy = request.GET['buy']
    _mark = request.GET['mark']
    mark = date + ' : ' + _mark

    if count > 0 and int(buy) < count:
        money = Money()
        money.name = name
        money.number = number
        money.charge = 0
        money.buy = buy
        money.mark = mark
        money.save()

        return get_all_money(request)
    else:
        return HttpResponse("您的账户余额不足，请充值后再尝试！")


# 以下对方法是对某账户金额的操作，姓名与账户为一对一关系。

def sum_count(sb_money):
    sum_charge = 0
    sum_buy = 0

    for sb in sb_money:
        sum_charge += sb.charge
        sum_buy += sb.buy

    count = sum_charge - sum_buy
    # 返回充值计数，消费计数，余额。
    return sum_charge, sum_buy, count

