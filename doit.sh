#!/bin/sh
./gendates.py | awk '{print $1}' | ./format_dates.sh | ./commits.sh
