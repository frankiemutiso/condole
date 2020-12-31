from django.shortcuts import render, redirect
from .models import Message, Death
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
            death.birth_year = form.cleaned_data['birth_year']
            death.death_year = form.cleaned_data['death_year']
            death.description = form.cleaned_data['description']

            death.save()

            return redirect('deaths')

    return render(request, 'condole/create_death.html', {'form': form})


def deaths(request):
    deaths = Death.objects.all()

    context = {'deaths':  deaths}

    return render(request, 'condole/deaths.html', context)


def detail(request, slug):
    death = Death.objects.get(slug=slug)
    messages = Message.objects.filter(owner=death.id)

    context = {'death': death, 'messages': messages}

    return render(request, 'condole/detail.html', context)


def leave_message(request, slug):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            death = Death.objects.get(slug=slug)
            message = Message()
            message.owner = Death.objects.get(slug=slug)
            message.name = form.cleaned_data['name']
            message.relationship_with_deceased = form.cleaned_data['relationship_with_deceased']
            message.email = form.cleaned_data['email']
            message.message = form.cleaned_data['message']

            message.save()

            return redirect('detail', death.slug)

    return render(request, 'condole/leave-message.html', {'form': form})
