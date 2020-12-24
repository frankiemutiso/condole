from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm, DeathForm
from django.shortcuts import render

# Create your views here.


def create_death(request):
    form = DeathForm()
    if request.method == 'POST':
        form = DeathForm(request.POST)
        if form.is_valid():
            death = Death()
            death.name = form.cleaned_data['name']
            death.age = form.cleaned_data['age']
            death.description = form.cleaned_data['description']

            death.save()

            return redirect('deaths')

    return render(request, 'condole/create_death.html', {'form': form})


def deaths(request):
    deaths = Death.objects.all()
    context = {'deaths':  deaths}

    return render(request, 'condole/deaths.html')


def post_message(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message()
            message.name = form.cleaned_data['name']
            message.relationship_with_deceased = form.cleaned_data['relationship_with_deceased']
            message.email = form.cleaned_data['email']
            message.message = form.cleaned_data['message']

            message.save()

            return redirect('condolences')

    return render(request, 'condole/create.html', {'form': form})


def condolences(request):
    condolences = Message.objects.all()
    context = {'condolences': condolences}

    return render(request, 'condole/messages.html', context)
