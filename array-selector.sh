#!/bin/bash

colors=("red" "blue" "green" "white" "black")

if [ $# -eq 1 ] && [[ $1 =~ ^[0-9]+$ ]] && [ $1 -le ${#colors[@]} ] && [ $1 -ne 0 ]; then
echo "${colors[$(($1 - 1))]}"
else
echo "Error"
fi