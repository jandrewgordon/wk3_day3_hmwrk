from app.models.beer import *

beer1 = Beer("Asahi Super Dry", "Asahi", 2.10, 'asahi_super_dry')
beer2 = Beer("Nastro Azzuro", "Peroni", 1.95, 'nastro_azzuro')
beer3 = Beer("Budweiser", "Budweiser Budvar", 2.10, 'budweiser')

beers = [beer1, beer2, beer3]

# def add_url_to_class(beers):
#     for beer in beers:
#         beer.url = make_url(beer.name)

# def make_url(beer_name):
#     spaceless_name = remove_space(beer_name)
#     beer_url = spaceless_name.lower()

# def remove_space(string):
#     for letter in list(string):
#         if letter == " ":
#             letter.remove()
#     return string

