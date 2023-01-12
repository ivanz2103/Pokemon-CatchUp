from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Pokemon,db
from app.pokemon.forms import CreatePokemon
import requests

pokemon = Blueprint('pokemon', __name__, template_folder='pokemon_template')

@pokemon.route('/create/', methods=['GET', 'POST'])
def create():
    form = CreatePokemon()
    pokemonPokedex = {}
    if request.method == "POST":
        if form.validate():
            pokemon = form.pokemon.data
            print(pokemon)
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
            response = requests.get(url)
            if response.ok:
                data = response.json()
                pokemonPokedex = {
                    'name': data['forms'][0]['name'],
                    'ability': data['abilities'][1]['ability']['name'],
                    'base_experience': data['base_experience'],
                    'sprite_url': data['sprites']['front_shiny'],
                    'attack_base': data['stats'][1]['base_stat'],
                    'hp_base': data['stats'][0]['base_stat'],
                    'defense_base': data['stats'][2]['base_stat']
                }
                print(pokemonPokedex)
            else:
                print('ERROR you have input an incorrect pokemon name please try again 😊.')
            pokemon = Pokemon(pokemonPokedex['name'], pokemonPokedex['ability'], pokemonPokedex['base_experience'], pokemonPokedex['sprite_url'], pokemonPokedex['attack_base'], pokemonPokedex['hp_base'], pokemonPokedex['defense_base'])
            db.session.add(pokemon)
            db.session.commit()
            return render_template('create.html', form=form, pokemonPokedex=pokemonPokedex)

    return render_template('create.html', form=form, pokemonPokedex=pokemonPokedex)