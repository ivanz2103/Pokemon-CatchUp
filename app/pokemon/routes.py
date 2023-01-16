from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Pokemon, db
from app.pokemon.forms import CreatePokemon
import requests
from flask_login import current_user, login_required


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
                    'sprite_url': data['sprites']['front_default'],
                    'attack_base': data['stats'][1]['base_stat'],
                    'hp_base': data['stats'][0]['base_stat'],
                    'defense_base': data['stats'][2]['base_stat']
                }
                print(pokemonPokedex)
            else:
                print('ERROR you have input an incorrect pokemon name please try again 😊.')
            pokemon = Pokemon(pokemonPokedex['name'], pokemonPokedex['ability'], pokemonPokedex['base_experience'], pokemonPokedex['sprite_url'], pokemonPokedex['attack_base'], pokemonPokedex['hp_base'], pokemonPokedex['defense_base'], current_user.id)
            db.session.add(pokemon)
            db.session.commit()
            return render_template('create.html', form=form, pokemonPokedex=pokemonPokedex)

    return render_template('create.html', form=form, pokemonPokedex=pokemonPokedex)
    
@pokemon.route('/view')
def view():
    pokemon = Pokemon.query.all()
    return render_template('view.html', pokemon=pokemon [::-1])

@pokemon.route('/create/')
def ok():
    pokemon = Pokemon.query.all()
    if pokemon.isintance <= 5:
        pokemon.save_to_db()
    else:
        flash('You have reached the maximum number of pokemon 😊')
        redirect(url_for('/pokeball.html'))
    return render_template('create.html', pokemon=pokemon)


@pokemon.route('/create/<int:pokemon_id>')
def edit(pokemon_id):
    pokemonPokedex = Pokemon.query.get(pokemon_id)
    if pokemonPokedex:
        global pokemon_int
        pokemon_int = int(pokemon_id)
        return render_template('edit.html',pokemon_int=pokemon_int, pokemonPokedex=pokemonPokedex)
    else:
        return redirect(url_for('pokemon.create'))

pokemon_int = 0

@pokemon.route('/create/update/<int:pokemon_id>', methods=['GET', 'POST'])
def update_pokemon(pokemon_id):
    form = CreatePokemon()
    pokemon = Pokemon.query.get(pokemon_id)
    if current_user.id == pokemon.user_id:
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

                    db.session.commit()
            return redirect(url_for('pokemon.view'))

    return render_template('update_pokemon.html', form=form, pokemon=pokemon)

@pokemon.route('/create/delete/<int:pokemon_id>')
def delete_pokemon(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    if pokemon:
        db.session.delete_from_db(pokemon)
        db.session.commit()
    return redirect(url_for('pokemon.view'))

@pokemon.route('/pokeball')
@login_required
def pokeball():
    pokemon  = Pokemon.query.all()
    
    return render_template('pokeball.html', pokemon=pokemon)