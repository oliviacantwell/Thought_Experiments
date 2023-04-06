from django.shortcuts import render
import random
# Create your views here.

def prisoner(request):
    return render(request,'prisoner.html')

opponentScore = 0
playerScore = 0

def opponentChoice(request): 
    Osteal = 1
    Osplit = 2
    text = ""
    choice = random.randInt(Osteal,Osplit)
    if choice == 1:
        text = "Steal!"
    else: 
        text = "Split!"
    # return render(request, "prisoner.html",{'text':text})
    return text


def playerScore():
    tes = ""