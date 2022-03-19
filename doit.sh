#!/bin/sh
./gendates.py || exit 1
cat dates | ./commits.sh || exit 1
