#!/bin/bash

nohup grep "moon" facts && echo "The moon fact was found!" > output.txt &