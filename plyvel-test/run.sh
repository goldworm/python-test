#!/bin/bash

# 2.5 hours
rm -f result.log
python read-write-test.py 10000000 hx1b8959dd5c57d2c502e22ee0a887d33baec09091 ./icon_dex
