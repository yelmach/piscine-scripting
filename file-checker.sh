#!/bin/bash

if [ ! $# -eq 1 ]; then
    echo "Error: No file provided"
    exit 0
fi

if [ -e $1 ]; then
    echo "File exists"

    if [ -r $1 ]; then
        echo "File is readable"
    else
        echo "File is not readable"
    fi

    if [ -w $1 ]; then
        echo "File is writable"
    else
        echo "File is not writable"
    fi

    if [ -x $1 ]; then
        echo "File is executable"
    else
        echo "File is not executable"
    fi
else
    echo "File does not exist"
fi