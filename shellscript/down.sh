#!/bin/bash
for comp in `cat comp`
for vers in `cat vers`
do
wget -c https://pypi.python.org/pypi/$comp/$vers --no-check-certificate
echo $comp
done
