#!/bin/bash

pip install --upgrade pip

if [ "${BUILD}" != "flake8" ]; then
    git clone https://github.com/JHUISI/charm.git
    cd charm && git checkout 2.7-dev
    ./configure.sh
    python setup.py install
    cd ..
fi

if [ "${BUILD}" == "tests" ]; then
    pip install -e .[test]
    pip install --upgrade codecov
elif [ "${BUILD}" == "docs" ]; then
    pip install -e .[docs]
elif [ "${BUILD}" == "flake8" ]; then
    pip install flake8
fi
