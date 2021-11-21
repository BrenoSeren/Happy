from django.shortcuts import render
import folium
import geocoder

# Create your views here.
def map(req):
    adress = req.POST.get('adress')
    if adress == None:
        adress = 'São Paulo'
    location = geocoder.osm(adress)
    lat = location.lat
    lng = location.lng
    country = location.country
    # Create Map Object
    m = folium.Map(location=[-15.7801,-47.9292], zoom_start=4)
    folium.Marker([lat,lng], tooltip='Clique para mais informações', popup=country).add_to(m)
    m = m._repr_html_()
    context={
        'm':m,
    }
    return render(req, 'map.html', context)
