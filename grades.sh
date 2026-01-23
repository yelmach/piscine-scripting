#!/bin/bash

if [ $# -ne 1 ] || [[ ! $1 =~ ^[0-9]+$ ]]; then
    echo "Error: expect 1 argument only!" >&2
    exit 1
fi

declare -a students

for (( i = 1; i <= $1; i++ ))
do
    read -p "Student Name #$i: " name
    read -p "Student Grade #$i: " grade

    if [[ ! $grade =~ ^[0-9]+$ ]] || [ "$grade" -gt 100 ]; then
        echo "Error: The grade '$grade' is not a valid input. Only numerical grades between 0 and 100 are accepted." >&2
        exit 1
    fi

    if [ "$grade" -ge 90 ]; then
        result="You did an excellent job!"
    elif [ "$grade" -ge 70 ]; then
        result="You did a good job!"
    elif [ "$grade" -ge 50 ]; then
        result="You need a bit more effort!"
    else
        result="You had a poor performance!"
    fi

    students+=("$name: $result")
done

for (( i = 0; i < $1; i++ ))
do
    echo ${students[i]}
done