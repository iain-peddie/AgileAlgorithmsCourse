#!/usr/bin/env bash

echo "$0"
thisdir=`dirname $0`
PYTHONPATH=$PYTHONPATH:$thisdir/../src
python3 $thisdir/runAllTests.py

