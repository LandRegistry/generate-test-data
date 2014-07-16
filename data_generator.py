import json


class DataGenerator(object):
    @staticmethod
    def loadJson():
        with open("source-data.json") as json_file:
            return json.load(json_file)

    @staticmethod
    def convertItem(raw_data_item):
        return {
            'title_id': 'TEST_' + raw_data_item[0],

            'proprietors': [
                {
                    'first_name': raw_data_item[4],
                    'last_name': raw_data_item[5]
                },
                {
                    'first_name': raw_data_item[6],
                    'last_name': raw_data_item[7]
                }
            ],

            'property' : {
                'address': {
                    'line_1': raw_data_item[3],
                    'line_2': raw_data_item[4],
                    'postcode': raw_data_item[5],
                },

                'tenure': raw_data_item[8]
            },

            'payment': {
                'price_paid': raw_data_item[10],
                'titles': ['TEST_' + raw_data_item[0]]
            }

        }
