from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from friends.models import Friend
# Create your views here.


def index(request):
    return render_to_response('index.html')


def friends(request):
    return render_to_response('friends.html')


def add_friend(request):
    return render(request, 'add_friend.html')


def create_friend(request):
    name = request.POST['name']
    sex = request.POST['sex']
    age = request.POST['age']
    phone = request.POST['phone']
    email = request.POST['email']
    live = request.POST['live']
    address = request.POST['address']
    mark = request.POST['mark']

    friend = Friend()
    friend.name = name
    friend.sex = sex
    friend.age = age
    friend.phone = phone
    friend.email = email
    friend.live = live
    friend.address = address
    friend.mark = mark
    friend.save()

    # return HttpResponse("This data has been saved ok! Thanks.")
    return get_all_friends(request)


def get_all_friends(request):
    error = True
    all_friends = Friend.objects.all()
    if not all_friends:
        error = False
    return render_to_response('all_friends.html', {'friends': all_friends, 'error': error})


def get_all_friends_sex(request):
    girl_friends = Friend.objects.filter(sex=0)
    boy_friends = Friend.objects.filter(sex=1)
    return render_to_response('friends_msg.html', {'girl_friends': girl_friends, 'boy_friends': boy_friends})


def delete_friend(request):
    _id = request.GET['delete']
    Friend.objects.get(id=int(_id)).delete()
    return get_all_friends(request)


def get_one_friend(request):
    _id = request.GET['editor']
    friend = Friend.objects.get(id=int(_id))
    return render(request, 'update_friend.html', {'friend': friend})


def update_friend(request):
    _id = request.POST['id']
    friend = Friend.objects.get(id=int(_id))

    friend.name = request.POST['name']
    # friend.sex = request.POST['sex']
    friend.age = request.POST['age']
    friend.phone = request.POST['phone']
    friend.email = request.POST['email']
    friend.live = request.POST['live']
    friend.address = request.POST['address']
    friend.mark = request.POST['mark']
    friend.save()

    return get_all_friends(request)


def search(request):
    return render(request, 'search_friend.html')


def search_friend(request):
    error = True
    name = request.GET['name']
    friends = Friend.objects.filter(name=name)
    if not friends:
        error = False
        # return search(request)
    return render_to_response('search_results.html', {'friends': friends, 'error': error})

