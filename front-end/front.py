from flask import Flask, render_template, render_template_string, request, redirect, url_for, flash
from flask_pymongo import pymongo
import folium

from folium.map import Marker
from geopy.geocoders import Nominatim
import geopy.exc

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)
app.secret_key = "79e0fd755bf9ecd99d5af5bfa6e659b71d68f84d"

MONGO_URI = "mongodb+srv://danielsarmiento:nG9xkw5b3zkJhf3@epita.xqy9hdp.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_URI)

db = client.get_database('my-travel-map')
user_collection = pymongo.collection.Collection(db, 'user_collection')

def flask_mongodb_atlas():
    return "flask mongodb atlas!"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        existing_username = db.user_collection.find_one({"username": username})
        if existing_username:
            return redirect(url_for('visited', username=username))
        else:
            db.user_collection.insert_one({"name": username})
            return redirect(url_for('visited', username=username))
        
    else:
        return render_template('index.html')

geolocator = Nominatim(user_agent="travel-mapper")
visited_cities = []  # Liste des villes visitées

@app.route('/visited/<username>', methods=['GET', 'POST'])
def visited(username):
    visited_cities.clear()

    if request.method == 'GET':
        # Création de la map
        m = folium.Map()
        m.get_root().width = "800px"
        m.get_root().height = "600px"

        # Récupérer toutes les villes de la base de données pour l'utilisateur courant
        cities = db.city_collection.find({"username": username})

        # Ajouter les villes à la liste visited_cities
        for city in cities:
            city_data = (city["city"], city["latitude"], city["longitude"])
            if city_data not in visited_cities:
                visited_cities.append(city_data)

        # Ajout de tous les marqueurs sur la map
        for city, lat, lon in visited_cities:
            folium.Marker([lat, lon], popup=city).add_to(m)
        iframe = m.get_root()._repr_html_()

        return render_template('visited.html', cities=visited_cities, iframe=iframe, username=username)


    if request.method == 'POST':
        city = request.form['city']

        try:
            location = geolocator.geocode(city)

            if location:
                existing_city = db.city_collection.find_one({"username": username, "city": city})

                if existing_city:
                    flash(f"{city} is already in the list.")
                    return redirect(url_for('visited', username=username))
                else:
                    visited_cities.append((city, location.latitude, location.longitude))
                    db.city_collection.insert_one({"username" : username , "city": city,
                                                  "latitude" : location.latitude, "longitude" : location.longitude})
                    flash(f"{city} has been added.")
                    return redirect(url_for('visited', username=username))
            else:
                flash(f"{city} coordinates cannot be found.")
                return redirect(url_for('visited', username=username))
        
        except geopy.exc.GeocoderUnavailable:
            flash("The geolocalisation service is currently unavailable please retry again.")
            return redirect(url_for('visited', username=username))

    return render_template('visited.html', cities=visited_cities, username=username)
    
#test to insert data to the data base
@app.route("/test")
def test():
    location_center = [51.7678, -0.00675564]
    m = folium.Map(location_center, zoom_start=13)
      
    m.add_child(folium.ClickForMarker(popup="Waypoint"))
    map_html = m._repr_html_()
    return {"map": map_html}


    m = folium.Map(location=[45.372, -121.6972],
                zoom_start=15)

    # set the iframe width and height
    m.get_root().width = "800px"
    m.get_root().height = "600px"

    folium.Marker(
    [45.372, -121.6972], popup="<i>Italic popup text</i>", tooltip="Click on Marker"
    ).add_to(m)
    
    folium.Marker(  # Marker with icon
    location=[45.371, -121.683],
    popup="<b>Bold popup text</b>",
    tooltip="Click on Marker",
    ).add_to(m)

    
    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    
    MousePosition(
    position="topright",
    separator=" | ",
    empty_string="NaN",
    lng_first=True,
    num_digits=20,
    prefix="Coordinates:",
    lat_formatter=formatter,
    lng_formatter=formatter,
    ).add_to(m)

    
    m.add_child(folium.ClickForMarker(popup="new marker"))


    m.save

    iframe = m.get_root()._repr_html_()

    return render_template('teste.html',
        iframe=iframe
    )

# @app.route('/visited', methods=['GET', 'POST'])
# def visited():
    if request.method == 'GET':
            # Créez une carte Folium avec les marqueurs des villes visitées
        m = folium.Map()
        m.get_root().width = "800px"
        m.get_root().height = "600px"
               
        # Récupérer toutes les villes de la base de données pour l'utilisateur "milk"
        cities = db.city_collection.find({"username": "milk"})
        
        # Ajouter les villes à la liste visited_cities
        for city in cities:
            city_data = (city["city"], city["latitude"], city["longitude"])
            if city_data not in visited_cities:
                visited_cities.append(city_data)
        
        for city, lat, lon in visited_cities:
            folium.Marker([lat, lon], popup=city).add_to(m)
        iframe = m.get_root()._repr_html_()

        return render_template('visited.html', cities=visited_cities, iframe=iframe) 
    
    
    if request.method == 'POST':
        city = request.form['city']
        location = geolocator.geocode(city)
        existing_city = db.city_collection.find_one({"username": "milk", "city": city})
        if location:
            if existing_city:
                flash(f"{city} is already in the list.")
                return redirect(url_for("visited"))
            else:
                visited_cities.append((city, location.latitude, location.longitude))
                db.city_collection.insert_one({"username" : "milk" , "city": city,
                                              "latitude" : location.latitude, "longitude" : location.longitude})
                flash(f"{city} has been added.")                              
                return redirect(url_for("visited"))
        else:
            return "Cannot find the city coordinates."

    return render_template('visited.html', cities=visited_cities)


@app.route('/delete/<username>', methods=['POST'])
def delete_entries(username):
    # Supprimer toutes les entrées pour l'utilisateur actuel dans la base de données
    db.city_collection.delete_many({"username": username})
    flash("All entries have been deleted.")
    return redirect(url_for('visited', username=username))
