from django.shortcuts import render
from board_m.models import Board


# Create your views here.
def index(request):
    templates='index.html'
    return render(request, templates)

def board(request):
    templates= 'board.html'
    
    try:
        my_board= Board.objects.filter(creater=request.user)
    except:
        my_board="you have no any Board"
    context= {'boards':my_board}
    return render(request,templates,context)