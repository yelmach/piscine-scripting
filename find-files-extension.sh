#!/bin/bash
find . -type f -name "*.txt" -exec basename {} .txt \;

# find . -iregex '.*\.\(txt\)' -printf "%f\n" | cut -d "." -f 1