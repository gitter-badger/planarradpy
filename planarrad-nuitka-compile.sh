#!/usr/bin/env bash
chrt --verbose --idle 0 ionice --ignore --class 3 nuitka --recurse-all --standalone --python-version=2.7 --jobs=8 --output-dir="/home/marrabld" "/home/marrabld/Projects/planarradpy/planarrad.py"