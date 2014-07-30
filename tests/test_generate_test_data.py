import unittest
from data_generator import DataGenerator

class GenerateTestDataTestCase(unittest.TestCase):
    def setUp(self):
        self.data = DataGenerator.load_json()

    def test_can_parse_raw_data(self):
        self.assertFalse(self.data is None)

    def test_can_convert_single_item(self):
        
        raw_data_item = [
            "SM7333269",
            "376-8006",
            "Enim. Road",
            "Raurkela Civil Township",
            "L95 4ZD",
            "Denise",
            "Bates",
            "Kerry",
            "Myers",
            "freehold",
            "good",
            "208648",
            {
                "type": "Feature",   
                "crs": {
                        "type": "name",     
                        "properties": {
                                        "name": "urn:ogc:def:crs:EPSG:27700"
                                       }
                        },
                        "geometry": {
                                        "type": "Polygon",
                                        "coordinates": [[ [530857.01, 181500.00], [530857.00, 181500.00], [530857.00, 181500.00], [530857.00, 181500.00], [530857.01, 181500.00] ]       ]
                                    },
                        "properties" : {}
                    }
        ]

        title = DataGenerator.convert_item(raw_data_item)
        self._check_title_structure(title, raw_data_item[0])

        expected_title = {
            'title_number': 'TEST_' + raw_data_item[0],

            'proprietors': [
                {
                    'first_name': raw_data_item[5],
                    'last_name': raw_data_item[6]
                },
                {
                    'first_name': raw_data_item[7],
                    'last_name': raw_data_item[8]
                }
            ],

            'property': {
                'address': {
                         'house_number': raw_data_item[1],
                        'road': raw_data_item[2],
                        'town': raw_data_item[3],
                        'postcode' : raw_data_item[4]
                },

                'tenure': raw_data_item[9],
                'class_of_title': raw_data_item[10]
            },

            'payment': {
                'price_paid': raw_data_item[11],
                'titles': ['TEST_' + raw_data_item[0]]
            },
            'extent': {
                "type": "Feature",   
                "crs": {
                        "type": "name",     
                        "properties": {
                                        "name": "urn:ogc:def:crs:EPSG:27700"
                                       }
                        },
                        "geometry": {
                                        "type": "Polygon",
                                        "coordinates": [[ [530857.01, 181500.00], [530857.00, 181500.00], [530857.00, 181500.00], [530857.00, 181500.00], [530857.01, 181500.00] ]       ]
                                    },
                        "properties" : {}
                    }
        }

        self.assertEqual(expected_title, title)

    def test_can_convert_all_data(self):
        raw_data_and_titles = zip(self.data, map(DataGenerator.convert_item, self.data))
        converted = map(lambda tuple: self._check_title_structure(tuple[1], tuple[0][0]), raw_data_and_titles)

        self.assertTrue(len(converted) == len(raw_data_and_titles))

    # ----------- Private helper methods -----------------

    def _check_title_structure(self, title, original_title_number):
        title_number = title.get('title_number')
        self.assertEqual('TEST_' + original_title_number, title_number)

        self._check_proprietors_structure(title.get('proprietors'))
        self._check_property_structure(title.get('property'))
        self._check_payment_structure(title.get('payment'), title_number)

    def _check_payment_structure(self, payment, title_number):
        self.assertTrue(payment is not None)

        price_paid = payment.get('price_paid')
        self.assertTrue(price_paid is not None)
        self.assertTrue(price_paid > 1000000)

        titles = payment.get('titles')
        self.assertTrue(len(titles) is 1)
        self.assertTrue(titles[0] == title_number)

    def _check_address_structure(self, address):
        self.assertTrue(address is not None)

        self.assertTrue(address.get('house_number') is not None)
        self.assertTrue(address.get('road') is not None)
        self.assertTrue(address.get('town') is not None)
        self.assertTrue(address.get('postcode') is not None)

    def _check_tenure_structure(self, tenure):
        self.assertTrue(tenure is not None)

        self.assertTrue(tenure == 'freehold' or tenure == 'leasehold')

    def _check_class_of_title_structure(self, class_of_title):
        self.assertTrue(class_of_title is not None)

        self.assertTrue(class_of_title == 'absolute' or
                        class_of_title == 'good' or
                        class_of_title == 'qualified' or
                        class_of_title == 'possesory')

    def _check_property_structure(self, property):
        self.assertTrue(property is not None)

        self._check_address_structure(property.get('address'))
        self._check_tenure_structure(property.get('tenure'))
        self._check_class_of_title_structure(property.get('class_of_title'))

    def _check_proprietors_structure(self, proprietors):
        self.assertTrue(len(proprietors) is 2)
        map(self._check_proprietor_structure, proprietors)

    def _check_proprietor_structure(self, proprietor):
        self.assertTrue(proprietor.get('first_name') is not None)
        self.assertTrue(proprietor.get('last_name') is not None)




