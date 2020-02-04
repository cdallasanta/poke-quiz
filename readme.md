# Pokemon Type Effectiveness Quiz

This is a cli game written in Python3 to test your pokemon knowledge.
There are two options to customize the difficulty:
1. Show the pokemon's name only, or it's name and type

    `e.g. "Abra" vs "Abra, type: psychic"`
2. When guessing, do you need one correct answer, or all possible correct answers

    `e.g. "bug" vs "bug, dark, ghost"`

### How to run:
To run, clone this repo to your machine, then run `python3 app.py`. The cli will handle the rest.

### Notes:
This currently only uses generations 1-7, since it scrapes from www.pokemon.com/pokedex for the pokemons' weaknesses. Oddly enough, they have not updated their website to include Gen 8 yet.