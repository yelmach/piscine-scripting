#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Error: expect 2 arguments" >&2
    exit 1
fi

FLAG=$1
USERNAME=$2

USER_DATA=$(getent passwd $USERNAME)

case "$FLAG" in
    "-e")
        if [[ -n "$USER_DATA" ]]; then
            echo "yes"
        else
            echo "no"
        fi
        ;;
    "-i")
        if [[ -n "$USER_DATA" ]]; then
            echo "$USER_DATA"
        fi
        ;;
    *)
        echo "Error: unknown flag" >&2
        exit 1
        ;;
esac