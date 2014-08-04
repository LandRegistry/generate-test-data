#!/bin/bash

echo "Running with new dev environment"
source /vagrant/script/dev-env-functions
create_virtual_env "generate-test-data"
python loader.py $@
deactivate
