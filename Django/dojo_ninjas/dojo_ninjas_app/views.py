from django.shortcuts import render, redirect
from .models import Dojo
from .models import Ninja
from django.http import Http404


def index(request):
    all_dojos = Dojo.objects.all().order_by('name')
    dojo_ninjas = {}
    
    for dojo in all_dojos:
        dojo_ninjas[dojo] = dojo.ninjas.all()

    return render(request, 'index.html', {'all_dojos': all_dojos, 'dojo_ninjas': dojo_ninjas})

def create_dojo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        state = request.POST.get('state')
    
    new_dojo = Dojo.objects.create(
        name= name,
        city=city,
        state=state,
    )
    
    all_dojos = Dojo.objects.all().order_by('name')
    dojo_ninjas = {}
    
    for dojo in all_dojos:
        dojo_ninjas[dojo] = dojo.ninjas.all()
    
    return render (request,'index.html', {'all_dojos': all_dojos, 'dojo_ninjas': dojo_ninjas})

def create_ninja(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dojo_id = request.POST.get('dojo')
    
    dojo = Dojo.objects.get(id = dojo_id)
    
    new_ninja = Ninja.objects.create(
        first_name= first_name,
        last_name=last_name,
        dojo=dojo,
    )
    
    all_dojos = Dojo.objects.all().order_by('name')
    dojo_ninjas = {}
    
    for dojo in all_dojos:
        dojo_ninjas[dojo] = dojo.ninjas.all()
    
    return render (request,'index.html', {'all_dojos': all_dojos, 'dojo_ninjas': dojo_ninjas})


# def delete_dojo(request):
#     id = 'id'
#     dojo_to_delete = Dojo.objects.get(id = 'id')
#     dojo_to_delete.delete()
def delete_dojo(request, dojo_id):
    try:
        dojo_to_delete = Dojo.objects.get(id=dojo_id)
    except Dojo.DoesNotExist:
        raise Http404("Dojo does not exist")
    
    dojo_to_delete.delete()
    
    return redirect( '/')