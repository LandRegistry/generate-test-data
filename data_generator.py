
import json


class DataGenerator(object):
    @staticmethod
    def load_json():
        with open("source-data.json") as json_file:
            return json.load(json_file).get('data')

    @staticmethod
    def convert_item(raw_data_item):
        try:
            return {
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

                'property' : {
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
                }
            }
        except:
            print raw_data_item

