from django.shortcuts import render
import folium
import geocoder

# Create your views here.
def map(req):
    # implement DB
    # adress = req.POST.get('address')
    location = geocoder.osm('adress')
    lat = location.lat
    lng = location.lng
    country = location.country
    # Create Map Object
    m = folium.Map(location=[19,-12], zoom_start=2)
    folium.Marker([lat,lng], tooltip='Click for more information', popup=country).add_to(m)
    m = m._repr_html_()
    context={
        'm':m,
    }
    return render(req, 'map.html', context)
