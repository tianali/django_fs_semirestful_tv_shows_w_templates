from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
# Create your views here.
def home(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new_show(request):
    return render(request, 'create.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/create')

    show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description']
    )
    return redirect(f'/shows/{show.id}')

def read(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'read.html', context)

def edit(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/{{show.id}}/edit')
    show = Show.objects.get(id=id)
    show.title = request.POST['title'],
    show.network = request.POST['network'],
    show.release_date = request.POST['release_date'],
    show.description = request.POST['description']
    show.save()
    return redirect(f'/shows/{{show.id}}')

def destroy(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')