from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def trolly(request):
    return render(request,'trolly.html')

def questions(request):
    question = [
        {'quest': 'this is the text for q 1',
         'option_one' : 'option 1',
         'option_two':'option 2',
         'option_three':'option 3'},
        #  {'quest': 'this is the text for q 2',
        #   'option_one':'option 1.2',
        #   'option_two':'option 2.2',
        #   'option_three':'option 3.2'}

    ]
    
    # context = {'question':question}
    return render(request, 'trolly.html', question)
