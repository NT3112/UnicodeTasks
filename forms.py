from django import forms

class PokemonTypeForm(forms.Form):
    type_choices = (
        ('electric', 'Electric'),('normal','Normal'),('Fighting','fighting'),("poison","Poison"),( "ground","Ground"),("rock","Rock"),("bug","Bug"),( "ghost","Ghost"),("steel","Steel"),
          ("water","Water"),( "grass","Grass"), ("electric","Electric"),("psychic","Psychic"), ("ice","Ice"), ("dragon","Dragon"),("dark","Dark"), ("fairy","Fairy"), ("unknown","Unknown"), 
          ("shadow","Shadow"),
        ('fire', 'Fire'),
        
        
    )
    pokemon_type = forms.ChoiceField(choices=type_choices, label='Select a Pokemon Type')