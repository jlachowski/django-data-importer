#!/bin/bash

echo "This is a helper script to test against many environ versions."
echo "This script test against Django 1.3.x and 1.4.x using sqlite. It depends of pip."

OLD_DJANGO="$(pip freeze | grep Django)"

test_13() {
	echo "Testing against Django 1.3.x ..."
	pip install -q -U Django\<1.4.0
	python runtests.py --failfast --noinput -v0 && return 0 || return 1
}

test_14() {
	echo "Testing against Django 1.4.x ..."
	pip install -q -U Django\<1.5.0
	python runtests.py --failfast --noinput -v0 && return 0 || return 1
}

test_13 && test_14

result=$?

if [[ "$OLD_DJANGO" ]];
then
	pip install -q -U "$OLD_DJANGO"
	echo "$OLD_DJANGO reinstalled"
else
	pip uninstall Django
fi

exit $result
