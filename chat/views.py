from django.shortcuts import redirect, render
from .models import Messages, Room

# Create your views here.

def index(request):
    return render(request,'index.html')

def room(request, room):
    return render(request, 'chatroom.html')


def checkview(request):
    print("In check")
    username, room = (request.POST['username'], request.POST['room_id'])
    print(username, room)

    if Room.objects.filter(room_name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(room_name = room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
