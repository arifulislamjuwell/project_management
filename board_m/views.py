from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Board
from django.contrib.auth.models import User
# Create your views here.
def create_board(request):
    if request.method == "POST":
        name_list=''
        totalobject= User.objects.all()
        for name in totalobject:
            name_list += name.username+' '

        title= request.POST['tname']
        descrip=request.POST['descr']
        Board.objects.create(creater= request.user,title=title,descrip=descrip)


        return HttpResponse(name_list)