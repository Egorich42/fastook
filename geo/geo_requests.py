			

found_in_radius = """
SELECT name, ST_AsEWKT(point), ST_X(point), ST_Y(point), addres, id, dj_id
FROM cafes 
WHERE ST_DWithin(point,
				ST_GeomFromEWKT('SRID=4326;POINT({:f} {:f})'),
				{:f});


"""

test_taverns = """
SELECT * FROM taverns_taverna 
WHERE ST_DWithin(point,
				ST_GeomFromEWKT('SRID=4326;POINT({:f} {:f})'),
				{:f}); 

"""

ways_id_around = """
SELECT gid
FROM ways WHERE  ST_Distance(
	ST_Transform(ST_GeomFromText('POINT({lon} {lat})',4326),26986),
	ST_Transform( ST_GeomFromText(ST_AsText (ST_Transform (the_geom, 4326)), 4326),26986)
	) < 20  ORDER BY ST_Distance(
	ST_Transform(ST_GeomFromText('POINT({lon} {lat})',4326),26986),
	ST_Transform( ST_GeomFromText(ST_AsText (ST_Transform (the_geom, 4326)), 4326),26986)
	) ASC;
"""



dijkstra = """
SELECT 
   ST_AsText (ST_Transform (the_geom, 4326))
FROM  pgr_dijkstra('SELECT gid AS id, source,target, length AS cost FROM ways',{:d},{:d})
 as d                                         
    LEFT JOIN ways AS e ON d.edge = e.gid 
ORDER BY d.seq;  
"""

#------------FOR TEST---------------#
all_cafes = """
SELECT id, point, ST_X(point), ST_Y(point) 
FROM cafes;
"""

add_addr = """
UPDATE cafes 
SET addres = {cafe_addr}
WHERE id = {cafe_id}
AND point = {cafe_point}
"""



insert_cafe_from_fastook = """
INSERT INTO cafes(id, name,  addres, point, dj_id) 
VALUES ({id}, {name}, {adr}, ST_SetSRID(ST_MakePoint({lon}, {lat}),4326),  {dj_id});
"""



'''
cafe_coords = convert_adres(full_adress())

insert_cafe_from_fastook.format(
								id = self.id, 
								name = name, 
								adr = full_adress(),
								lon = cafe_coords['longitude'],
								lat = cafe_coords['latitude'], 
								dj_id = self.id,
								)
'''
#INSERT INTO cafes(id, name,point, lon, lat) VALUES (111111, 'Тестовая кафешечка', ST_SetSRID(ST_MakePoint(27.599893, 53.896199),4326),  27.599893, 53.896199);


#MAKE POINT FROM COOORS https://postgis.net/docs/ST_MakePoint.html

#SELECT ST_X(ST_MakePoint(27.611983,53.855813));
#SELECT ST_MakePoint(27.611983,53.855813);





