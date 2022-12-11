#!/bin/bash

# Find all IP addresses in the log file using grep
ip_addresses=$(grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" logfile.txt)

# Count the occurrences of each IP address
ip_counts=()
for ip in $ip_addresses; do
    found=0
    for entry in "${ip_counts[@]}"; do
        # Check if the IP address is already in the counts
        if [ "$ip" == "${entry[0]}" ]; then
            # Increment the count for this IP address
            ((entry[1]++))
            found=1
            break
        fi
    done

    # Add a new entry to the counts if the IP address was not found
    if [ $found -eq 0 ]; then
        ip_counts+=("$ip" 1)
    fi
done

# Print the IP addresses and their counts
for entry in "${ip_counts[@]}"; do
    printf "%s: %d\n" "${entry[0]}" "${entry[1]}"
done
