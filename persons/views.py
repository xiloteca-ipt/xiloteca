#from django.http import JsonResponse
#from django.shortcuts import render, redirect, get_object_or_404

#from .forms import PersonCreationForm
#from .models import Person , City
import json
from django.shortcuts import render
from .forms import PersonForm
from django.http import JsonResponse
import json
from .models import Madeira

def person(request):
    print("request")
    print(request)
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "persons/person.html", {"form": form})

def wood(request):
    data = json.loads(request.body)
    wood = Madeira.objects.filter(cod_nome_popular=data['user_id'])
    print("Sucess linha 26, Views.py")
    print(wood)
    return JsonResponse(list(wood.values("cod_madeira", "nome_popular")), safe=False)

def nomep(request):
    data = json.loads(request.body)
    nomep = Madeira.objects.filter(cod_nome_popular=data['user_id'])
    print("Sucess linha 32, Views.py")
    print(nomep)
    return JsonResponse(list(nomep.values("cod_nome_popular", "nome_popular")), safe=False)

#def person_create_view(request):
#    form = PersonCreationForm()
#    if request.method == 'POST':
#        form = PersonCreationForm(request.POST)
#        if form.is_valid():
##            form.save()
#            return redirect('person_add')
#    return render(request, 'persons/home.html', {'form': form})


#def person_update_view(request, pk):
#    person = get_object_or_404(Person, pk=pk)
#    form = PersonCreationForm(instance=person)
#    if request.method == 'POST':
#        form = PersonCreationForm(request.POST, instance=person)
#        if form.is_valid():
#            form.save()
#            return redirect('person_change', pk=pk)
#    return render(request, 'persons/home.html', {'form': form})


# AJAX
#def load_cities(request):
#    country_id = request.GET.get('country_id')
#    cidade = City.objects.filter(country_id=country_id).all()
#    return render(request, 'persons/city_dropdown_list_options.html', {'cities': cidade})
#    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

