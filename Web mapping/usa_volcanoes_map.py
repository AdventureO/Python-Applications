import folium, pandas

# Read data from file
df=pandas.read_csv('Volcanoes-USA.txt')

# Create a map object with some parameters
map=folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=5, tiles='Stamen Terrain')

# Create feature group
fg=folium.FeatureGroup('USA Volcanoes Locations')

# Add to feature group all markers
for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    fg.add_child(folium.Marker([lat, lon], popup=name,
                  icon=folium.Icon(color='green' if elev in range(0, 1500)
                  else 'orange' if elev in range(1000, 3000) else 'red')))

# Add feature group to map
map.add_child(fg)

# Add layer control
map.add_child(folium.LayerControl())

# Save map as html file
map.save(outfile='usa_volcanoes.html')
