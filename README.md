generate-test-data
==================

[![Build Status](https://travis-ci.org/LandRegistry/generate-test-data.svg)](https://travis-ci.org/LandRegistry/generate-test-data)

Generates test data in the format required by the mint using a json doc generated by generatetestdata.com

### How to run

In one window start everything from the development envrionment root directory

```
./start-all
```

From the development environment cd into the app directory

```
cd apps/generate-test-data
```

Then load the data

```
./load_test_data_into_dev_environment.sh
```

This should load the test data into the mint

To load only a certain number of titles, specify a command-line argument indicating the quantity, e.g.:

    ./load_test_data_into_dev_environment.sh 1

### Data schema

The current data schema for a title is as follows, with an example title:

<pre>
	{
            'title_number': "TEST_AB1234567",

            'proprietors': [
                {
                    'first_name': "firstname",
                    'last_name': "lastname"
                },
                {
                    'first_name': "firstname",
                    'last_name': "lastname"
                }
            ],

            'property' : {
                'address': {
                    'house_number': "house number",
                    'road': "road",
                    'town': "town",
                    'postcode': "<a postcode>"
                },

                'tenure': "freehold|leasehold",
                'class_of_title': "absolute|good|qualified|possesory"
            },

            'payment': {
                'price_paid': "12345",
                'titles': ["TEST_AB1234567"]
            },
            'extent': {"type": "Feature", "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG:27700"}}, 			"geometry": {"type": "Polygon", "coordinates": [[[530857.01, 181500.00], [530857.00, 181500.00], 			[530857.00, 181500.00], [530857.00, 181500.00], [530857.01, 181500.00] ]]}, "properties" : {      } }
        }
</pre>
