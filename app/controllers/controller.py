from flask import render_template
from app import app
from app.models.beer_list import beers

@app.route('/beers')
def index():
    return render_template('index.html', title='Home', beers = beers)

@app.route('/beers/<beer_name>')
def show_beer(beer_name):
    # add_url_to_class(beer_name)
    for beer in beers:
        if beer_name == beer.url:
            return render_template('order.html', title = beer.name, beer = beer)