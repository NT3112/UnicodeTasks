from django.shortcuts import render,HttpResponse
import requests
from django.http import JsonResponse

def index(request):
    return HttpResponse('this is homepage')

def random_pokemon_by_type(request):
    selected_type = None
    pokemon_data = None

    if request.method == 'POST':
        selected_type = request.POST.get('pokemon_type')
        if selected_type:
            #fetching pokemon data based on selected type
            response = requests.get(f'https://pokeapi.co/api/v2/type/{selected_type}/')
            
            if response.status_code == 200:
                data = response.json()
                # Extract relevant data from the response
                pokemon_data = data['pokemon']
            else:
                # Handle API request error
                pass
    return render(request, 'random_pokemon_by_type.html', {'selected_type': selected_type, 'pokemon_data': pokemon_data})


def pokemon_types(request):
    response = requests.get('https://pokeapi.co/api/v2/type/')
    pokemon_data = []
    if response.status_code == 200:
        types_data = response.json()
        types = types_data['results']
        return render(request, 'pokedex/types.html', {'types': types})
        
    else:
        return render(request, 'pokedex/error.html')
    