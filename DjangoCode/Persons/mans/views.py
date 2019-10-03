from django.shortcuts import render
from django.shortcuts import render_to_response
from mans.models import Cardsmsg

# Create your views here.


def index(request):
    return render_to_response('index.html')


def mans(request):
    return render_to_response('cards.html')


def add_cardmsg(request):
    return render(request, 'add_card.html')


def create_cardmsg(request):
    name = request.GET['hostname']
    number = request.GET['cardnumber']
    password = request.GET['usepassword']
    mark = request.GET['mark']

    Cardmsg = Cardsmsg()
    Cardmsg.hostname = name
    Cardmsg.cardnumber = number
    Cardmsg.usepassword = password
    Cardmsg.mark = mark
    Cardmsg.save()

    return get_cardsmsg(request)


def get_cardsmsg(request):
    error = True
    all_cardsmsg = Cardsmsg.objects.all()
    if not all_cardsmsg:
        error = False

    return render(request, 'all_cardsmsg.html', {'all_cards': all_cardsmsg, 'error': error})


def operating(request):
    all_cardsmsg = Cardsmsg.objects.all()
    return render_to_response('operate_cards.html', {'all_cards': all_cardsmsg})


def get_one_cardmsg(request):
    _id = request.GET['editor']
    Cardmsg = Cardsmsg.objects.get(id=int(_id))
    return render(request, 'update_cardmsg.html', {'card': Cardmsg})


def update_cardmsg(request):
    _id = request.GET['id']
    Cardmsg = Cardsmsg.objects.get(id=int(_id))

    Cardmsg.hostname = request.GET['hostname']
    Cardmsg.cardnumber = request.GET['cardnumber']
    Cardmsg.usepassword = request.GET['usepassword']
    Cardmsg.mark = request.GET['mark']
    Cardmsg.save()

    return get_cardsmsg(request)


def delete_cardmsg(request):
    _id = request.GET['delete']
    try:
        Cardsmsg.objects.get(id=int(_id)).delete()
    except:
        return get_cardsmsg(request)

    return get_cardsmsg(request)

