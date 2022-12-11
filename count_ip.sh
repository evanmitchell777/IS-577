#!/bin/bash

# check if a log file has been provided as an argument
if [ -z "$1" ]; then
  echo "Please provide a log file as an argument"
  exit 1
fi

# save the log file as a variable
log_file=$1

# create an array to store the IP addresses
ip_addresses=()

# use a regular expression to extract the IP addresses from the log file and store them in the array
while read -r line; do
  if [[ $line =~ [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3} ]]; then
    ip_addresses+=("$line")
  fi
done < "$log_file"

# loop through the array and count the number of times each IP address appears
for ip in "${ip_addresses[@]}"; do
  count=$(grep -o "$ip" <<< "${ip_addresses[@]}" | wc -l)
  echo "$ip appears $count times in the log file"
done
