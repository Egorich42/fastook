import geo
import unittest
https://pythonworld.ru/moduli/modul-unittest.html

busy_coords = (27.599893, 53.896199)
coords_to_addr   =  geo.coord_to_adr(busy_coords)
#print(coords_to_addr)


#print(type(haver))
 
class TestCoords(unittest.TestCase):    
    def setUp(self):
        self.addr_to_coords  = geo.convert_adres("Минск, Рокоссовского 12.")

    def test_LonNotNone(self):
        self.assertIsNotNone(type(self.addr_to_coords['longitude']), "Lon is None")


    def test_LatNotNone(self):
        self.assertIsNotNone(type(self.addr_to_coords['latitude']), "Lat is None")


    def tearDown(self):
        print('Finish!')





class TestHaver(unittest.TestCase):
    def setUp(self):
        self.haver = geo.haversine(57.23, 27.16,58.12, 28.16)

    def test_haverNotNone(self):
        self.assertNotEqual(self.haver, 0, "Haver is 0")


    @unittest.skip("demonstrating skipping")
    def test_haverNone(self):
        self.assertEqual(self.haver, 0, "Haver is 0")

    def test_haverIsFloat(self):
        self.assertEqual(type(self.haver), float, "Type is not float")


"""
python -m unittest -v test
python -m unittest test.TestCoords
python -m unittest test.TestHaver.test_haverNotNone

python -m unittest -v test.TestCoords
python -m unittest -v test.TestHaver.test_haverNotNone

python -m unittest -v --locals test.TestHaver.test_haverIsFloat

"""


if __name__ == '__main__':
    unittest.main()


