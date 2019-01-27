
import requests
import re
import psycopg2
from  . geo_settings import *
from . geo_requests import *

#from  geo_settings import *
#from geo_requests import *

from math import radians, cos, sin, asin, sqrt


#convert adres to geograf coordinats (string to lattitude and longitude) using Yandex API
def convert_adres(adres):
    clear_adres = re.sub(r'\([^()]*\)', '', adres)
    request = requests.get(req_to_yandex_api.format(clear_adres))
    if request.status_code == 200:
        req = request.json()
        if len(req['response']['GeoObjectCollection']['featureMember']) != 0:
            geo_dict = req['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')   

            result = {'longitude':float(geo_dict[0]), 'latitude':float(geo_dict[1])}
        else:
            result = {'longitude':None, 'latitude':None}

        return result
    else:
        return conect_error_message.format(request.status_code)
    pass


#convert coorods  to adres (lattitude and longitude to string) using Yandex API
def coord_to_adr(coords):
    req_to_yandex_api = 'https://geocode-maps.yandex.ru/1.x/?format=json&geocode={:f},{:f}&results=1'
    request = requests.get(req_to_yandex_api.format(float(coords[0]),float(coords[1]))).json()
    try:
        adres = request['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
        return ''.join(adres.split(',')[2:])
        
    except Exception:
        return 'address unknown'    
        pass


def create_locations_table(client_coords, radius):
    psql_conn = psycopg2.connect(database = DB['base_name'], user = DB['user_name'], password = DB['password'],  port = "5432")
    cur = psql_conn.cursor()

    objects_in_rad = found_in_radius.format(client_coords['lon'], client_coords['lat'], radius) 

    cur.execute(objects_in_rad)
    return(cur.fetchall())
    pass


#-------------------ТЕСТИМ ВЫБОРКУ ТАВЕРН-------------------#

def tavern_near(client_coords, radius):
    psql_conn = psycopg2.connect(database = 'dj_fast', user = 'egor_f', password = DB['password'],  port = "5432")
    cur = psql_conn.cursor()

    objects_in_rad = test_taverns.format(client_coords['lon'], client_coords['lat'], radius) 

    cur.execute(objects_in_rad)
    return(cur.fetchall())
    pass

#-------------------ТЕСТИМ ВЫБОРКУ ТАВЕРН-------------------#



def found_points_around(longitude, lattitude):
    psql_conn = psycopg2.connect(database = Geodata['base_name'], user = Geodata['user_name'], password = Geodata['password'],  port = "5432")
    cur = psql_conn.cursor()

    objects_in_rad = ways_id_around.format(lon = longitude, lat = lattitude) 

    cur.execute(objects_in_rad)
    return(cur.fetchall())    
    pass



def found_pdijkstra(id_start, id_end):
    psql_conn = psycopg2.connect(database = Geodata['base_name'], user = Geodata['user_name'], password = Geodata['password'],  port = "5432")
    cur = psql_conn.cursor()

    points_in_path = maps_sql.dijkstra.format(id_start, id_end) 

    cur.execute(points_in_path)
    return(cur.fetchall())    
    pass


def extract_addr_from_str(addres):
    return re.findall(r'[\d\.\d]+',addres)
    pass



def not_null_path(points_around_me, points_around_target):
    for x in points_around_target:
        if len(locator.found_pdijkstra(points_around_me[0][0], x[0])) > 3:
            return locator.found_pdijkstra(points_around_me[0][0], x[0])
            #break
        else:
            return False
            pass


def lat_lon_lists_create(list_of_points):
    lon_list = []
    lat_list = []


    for x in list_of_points:
        if x[0] != None:
            lust = extract_addr_from_str(x[0])
            if len(lust) != 0:
                for el in lust:
                    if not lust.index(el)%2:
                        lon_list += [el]
                    if lust.index(el)%2:
                        lat_list += [el]

    coords_list = []                
    for lat, lon in zip(lat_list, lon_list):
        coords_list += [[lat,lon]]

    return coords_list             
    pass




def haversine(lat1, lon1,  lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, (lon1, lat1, lon2, lat2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return round(km, 2)
    pass

# TEST----------------------------------------------------------------------------

def sel_all_cafes():
    psql_conn = psycopg2.connect(database = DB['base_name'], user = DB['user_name'], password = DB['password'],  port = "5432")
    cur = psql_conn.cursor()

    cur.execute(all_cafes)
    return(cur.fetchall())
    pass


def add_adreses_to_cafes():
    psql_conn = psycopg2.connect(database = DB['base_name'], user = DB['user_name'], password = DB['password'],  port = "5432")
    cur = psql_conn.cursor()

    for cafe in sel_all_cafes():
        addr_from_coords = coord_to_adr((cafe[2], cafe[3]))
        print(addr_from_coords)
        add_cafe_addres = add_addr.format(cafe_addr ="'"+addr_from_coords+"'", cafe_id = cafe[0], cafe_point = "'"+cafe[1]+"'")
        cur.execute(add_cafe_addres)

    psql_conn.commit()
    psql_conn.close()   



def dj_cafe_insert_cafes(command):
    psql_conn = psycopg2.connect(database = DB['base_name'], user = DB['user_name'], password = DB['password'],  port = "5432")
    cur = psql_conn.cursor()

    cur.execute(command)

    psql_conn.commit()
    psql_conn.close()   




#CREATE TABLE cafes(id SERIAL PRIMARY KEY, name TEXT, addres TEXT, dj_id INT);



#add_adreses_to_cafes()
#test = coord_to_adr([276.064935, 53.899747999999995])
#print(test)
#https://geocode-maps.yandex.ru/1.x/?format=json&geocode=27.6064935,53.899747999999995&results=1

    
#ALTER TABLE cafes ADD COLUMN address VARCHAR;


#SELECT ST_MakePoint(27.591626,53.870926);
"""
test_mesta = [
{'id': 100001,
'name':'TEST_shaurma',
'address':'проспект Рокоссовского, 145А микрорайон Серебрянка, Ленинский Минск, Беларусь',
'lon':53.855813, 
'lat':27.611983,
'point':'01010000003DB5FAEAAA9C3B40EE3EC7478BED4A40' 
},


{'id': 100002,
'name':'TEST_bliny',
'address':'проспект Рокоссовского, 119 микрорайон Серебрянка, Ленинский Минск, Беларусь',
'lon': 53.857203, 
'lat': 27.613610,
'point':'0101000000A27F828B159D3B403C84F1D3B8ED4A40'
},


{'id': 100003,
'name':'TEST_grill',
'address': 'переулок Козлова, 5АМинск, Беларусь',
'lon': 53.896585, 
'lat':27.600654,
'point': '01010000002A36E675C4993B40C68A1A4CC3F24A40'
},

{'id': 100004,
'name':'TEST_cofe', 
'address': '2-й Велосипедный переулок, 32 Минск, Беларусь',
'lon': 53.870926, 
'lat': 27.591626,
'point':'01010000009B7631CD74973B40389ECF807AEF4A40'
},
]


insert_test_data = """


#INSERT INTO cafes (id, name, ST_SetSRID(point,4326), address) 
#VALUES({}, {}, {}, {})
"""



def insert_test_cafes():
    psql_conn = psycopg2.connect(database = DB['base_name'], user = DB['user_name'], password = DB['password'],  port = "5432")
    cur = psql_conn.cursor()

    for mesto in test_mesta:
        insert_test = insert_test_data.format(mesto['id'], 
                                               "'"+mesto['name']+"'", 
                                               "'"+mesto['point']+"'", 
                                               "'"+mesto['address']+"'",
                                               )

        cur.execute(insert_test)

    psql_conn.commit()
    psql_conn.close()


insert_test_cafes()
"""