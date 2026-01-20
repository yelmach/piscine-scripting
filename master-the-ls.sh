#!/bin/bash
ls -pu | tr '\n' ',' | sed 's/,$//'