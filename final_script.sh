#!/bin/bash

logfile="/home/abraxas/Downloads"

echo -n "Enter the username you want to search for: "
read username

grep $username $logfile | awk '{print $11}' | sort | uniq -c | awk '{ if ($2 ~ /^[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*$/) { print $2 " " $1 } }'
