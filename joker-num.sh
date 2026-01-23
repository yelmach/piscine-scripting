#!/bin/bash

if [ $# -ne 1 ] || [[ ! $1 =~ ^[0-9]+$ ]] || [ $1 -gt 100 ] || [ $1 -lt 1 ]; then
    echo "Error: wrong argument"
    exit 1
fi

number=$1

for ((i = 5; i > 0;))
do
    echo "Enter your guess ($i tries left):"
    read guess
    
    if [[ ! $guess =~ ^[0-9]+$ ]] || [ $guess -gt 100 ] || [ $guess -lt 1 ]; then
        continue

    elif [ $guess -lt $number ]; then
        echo "Go up"

    elif [ $guess -gt $number ]; then
        echo "Go down"

    elif [ $guess -eq $number ]; then
        echo "Congratulations, you found the number in $(( 5 - $i + 1 )) moves!"
        exit
    fi

    ((i--))
done

echo "You lost, the number was $number"
