import folium
import json

# Charger le fichier GeoJSON
with open('points.geojson', 'r') as f:
    geojson_data = json.load(f)

# Créer une carte centrée autour de Paris
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Ajouter des marqueurs pour chaque point dans le fichier GeoJSON
for feature in geojson_data['features']:
    coords = feature['geometry']['coordinates']
    name = feature['properties']['name']
    folium.Marker([coords[1], coords[0]], popup=name).add_to(m)

# Sauvegarder la carte dans un fichier HTML
m.save('index.html')