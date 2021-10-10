from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.htm')

def music_player(request):
    return render(request,'music_player.htm')    
