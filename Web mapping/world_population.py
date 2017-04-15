import folium, pandas

df=pandas.read_csv('Volcanoes-USA.txt')
map=folium.Map(location=[], zoom_start=2, tiles='Mapbox bright')


map.add_child(folium.GeoJson(data=open('world-geojson-from-ogr.json', encoding='utf-8-sig'),
name='World population', style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <= 10000000
                            else 'orange' if 10000000 < x['properties']['POP2005'] <= 20000000 else 'red'}))


map.add_child(folium.LayerControl())
map.save('world_population.html')
