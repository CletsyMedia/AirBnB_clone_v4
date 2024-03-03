#!/usr/bin/python3
"""Flask App that integrates with AirBnB static HTML Template"""

from models.place import Place
import uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/3-hbnb')
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda ky: ky.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda ky: ky.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda ky: ky.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda ky: ky.name)
    cache_id = str(uuid.uuid4())

    return render_template('3-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


if __name__ == "__main__":
    """ Main Function """
    app.run(host=host, port=port)
