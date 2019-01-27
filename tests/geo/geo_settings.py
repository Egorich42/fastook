#DB ={'base_name': 'obj_data', 'user_name':'locator' , 'password':'password'}
DB ={'base_name': 'gis_test', 'user_name':'locator' , 'password':'password'}
Geodata ={'base_name': 'geo_data', 'user_name':'locator' , 'password':'password'}

req_to_yandex_api = 'https://geocode-maps.yandex.ru/1.x/?format=json&geocode={}&results=1'

ip_loactor = 'http://api.geoiplookup.net/?query={}'


#https://geocode-maps.yandex.ru/1.x/?format=json&geocode=Беларусь, Минск, пер. козлова 7г&results=1


"""
Козлова 7г
"27.595787 53.893774"


Уральский переулок, 13
53.900595, 27.607416


проспект Рокоссовского, 153
53.853666, 27.615609

проспект Рокоссовского, 156
53.853729, 27.611232
"""


'''

ALTER TABLE cafes ADD COLUMN lon DECIMAL, ADD COLUMN lat DECIMAL;
INSERT INTO cafes(id, name,point, lon, lat) VALUES (111111, 'Тестовая кафешечка', ST_SetSRID(ST_MakePoint(27.599893, 53.896199),4326),  27.599893, 53.896199);
INSERT INTO cafes(id, name,point, lon, lat) VALUES (222222, 'Тестовая кафешечка2', ST_SetSRID(ST_MakePoint(27.606316, 53.898926),4326), 27.606316, 53.898926);
INSERT INTO cafes(id, name,point, lon, lat) VALUES (333333, 'Тестовая кафешечка3', ST_SetSRID(ST_MakePoint(27.615973, 53.853667),4326), 27.615973, 53.853667);
INSERT INTO cafes(id, name,point, lon, lat) VALUES (444444, 'Тестовая кафешечка4', ST_SetSRID(ST_MakePoint(27.611256, 53.853614),4326), 27.611256, 53.853614);

'''
