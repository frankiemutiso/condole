from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.shortcuts import render

# Create your views here.


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
