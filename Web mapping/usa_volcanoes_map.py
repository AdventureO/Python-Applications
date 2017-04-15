import folium, pandas

df=pandas.read_csv('Volcanoes-USA.txt')
map=folium.Map(location=[df['LAT'].mean(), df['LON'].mean()], zoom_start=5, tiles='Stamen Terrain')

fg=folium.FeatureGroup('USA Volcanoes Locations')

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    fg.add_child(folium.Marker([lat, lon], popup=name,
                  icon=folium.Icon(color='green' if elev in range(0, 1500)
                  else 'orange' if elev in range(1000, 3000) else 'red')))

map.add_child(fg)
map.add_child(folium.LayerControl())

map.save(outfile='usa_volcanoes.html')
