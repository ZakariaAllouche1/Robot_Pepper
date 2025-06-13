import folium
import webbrowser

filepath = 'map.html'
m = folium.Map(location=[48.984580, 1.70188],zoom_start=100)
m.save(filepath)
webbrowser.open('file:///home/ros/'+filepath)
