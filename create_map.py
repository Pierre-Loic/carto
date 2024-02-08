import folium

# Créer une carte centrée autour de Paris
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Sauvegarder la carte dans un fichier HTML
m.save('index.html')