from django.shortcuts import render, get_object_or_404, render_to_response
from taverns.models import Taverna, Product
from django.views.generic.detail import DetailView
from clients.models import Owner as Client

from cart.forms import CartAddProductForm

import geo

def main(request):
	places = Taverna.objects.all()
	return render(request, 'places/taverns_list.html', {'places':places})
	pass


def show_tavern(request, slug):
	place = get_object_or_404(Taverna, slug=slug)
	products = Product.objects.filter(place=place)
	return render(request, 'places/taverna.html',{'place':place, 'products': products})
	pass



def show_product(request, slug):
	product = get_object_or_404(Product, slug=slug)
	cart_product_form = CartAddProductForm()
	return render(request, 'places/eda.html',{'product': product,'cart_product_form':cart_product_form})
	pass




def show_nearest_cafes(request):

	if request.method == 'POST':
		client_loc = request.POST['coords'].split(',')
		search_radius = float(request.POST['search_radius'])

		#accuracy = float(client_loc[2])
		lat = float(client_loc[0])
		lon = float(client_loc[1])
		places = geo.create_locations_table({'lat':lat, 'lon':lon},search_radius)  

		if request.POST['custom_adress']:
			if len(request.POST['custom_adress']) > 5:
				coords = geo.convert_adres('г.Минск,{}'.format(request.POST['custom_adress'])) 

				places = geo.create_locations_table({'lat': coords['latitude'], 'lon':coords['longitude']},search_radius)  
				lat = coords['latitude']
				lon = coords['longitude']        


		list_of_addr = []

		
		for place in places:
			if place[6] != None:
				list_of_addr += [
							{
							'name': place[0],
							'adres': place[4], 
							'coords':[place[2], place[3]], 
							'way_long': geo.haversine(lat,lon, place[3], place[2]),
							'marker':Taverna.objects.get(id=place[6]).get_absolute_url(),}]
			else:
				list_of_addr += [
							{
							'name': place[0],
							'adres': place[4], 
							'coords':[place[2], place[3]], 
							'way_long': geo.haversine(lat,lon, place[3], place[2]),
							'marker':'empty',
							}]




		list_of_addr = sorted(list_of_addr, key=lambda k: k['way_long']) 

		return render(request, 'places/nearest_places.html',  {'places':list_of_addr})
		pass
	else:
		return render(request, 'places/nearest_places.html', {'places':[]})
		pass




'''
https://postgis.net/docs/ST_MakePoint.html
ST_MakePoint(-71.1043443253471, 42.3150676015829);
add new_place into cafes  - name, coors, point, etc.
add field - lon, lat (from point to X or Y)




'''



#pg-U locator
#pg_dump -U locator gis_test > gis_test_work
"""
create user locator with password 'password';
create database obj_data owner locator;

grant all privileges on database obj_data to locator;


create database obj_data owner locator;



pg_dump -U locator gis_test > gis_test_work
psql dj_fast < fastook_work_base

create user egor_f with password 'password';
create database dj_fast owner egor_f;

        'NAME': 'dj_fast',
        'USER': 'egor_f',


        'NAME': 'dj_fast',
        'USER': 'egor_f',
        'PASSWORD': 'password',



ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO locator;
GRANT USAGE ON SCHEMA public to locator;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO locator;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO locator;
ALTER ROLE locator WITH Superuser;

CREATE TABLE obj_locations( obj_name VARCHAR, obj_type VARCHAR, obj_lon numeric, obj_lat numeric, obj_osm_id bigint);
"""
