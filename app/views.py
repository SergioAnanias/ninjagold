from django.shortcuts import render, redirect
from random import randint
from time import gmtime, strftime, localtime



def index(request):
    if not 'victory' in request.session or not request.session['victory']:
        pass
    if not 'gold' in request.session or not request.session['gold']:
        request.session['gold'] = 0
    if not 'message_list' in request.session or not request.session['message_list']:
        request.session['message_list'] = []
    context = {
        'gold' : request.session['gold'],
    }
    return render(request, 'index.html', context)

def victory(request):
    pass

def money(request):
    request.session['value'] = request.POST['processmoney']


    if request.session['value'] == 'Farm':

        numero = randint(10, 20)
        request.session['gold'] += numero
        request.session['message_list'].insert(0,numero)


    elif request.session['value'] == 'Cave':

        numero = randint(5, 10)
        request.session['gold'] += numero
        request.session['message_list'].insert(0,numero)


    elif request.session['value'] == 'House':

        numero = randint(2, 5)
        request.session['gold'] += numero
        request.session['message_list'].insert(0,numero)


    elif request.session['value'] == 'Casino':

        numero = randint(-50, 50)
        request.session['gold'] += numero
        request.session['message_list'].insert(0,numero)

    request.session.save()

    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['message_list'] = []
    return redirect('/')
    
def victoria(request):
    request.session['gold'] = 0
    request.session['message_list'] = []
    request.session['victoria'] = 0
    return render(request, 'victoria.html')
# Create your views here.
