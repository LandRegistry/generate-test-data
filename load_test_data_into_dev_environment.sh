#!/bin/bash

if [[ -f ./dev/run-command ]]; then
	echo "It looks like you're using the old dev environment"
	./dev/run-command python loader.py $@
else
	echo "Running with new dev environment"
	source /vagrant/script/checkout
	create_virtual_env "generate-test-data"
	python loader.py $@
	deactivate
fi
