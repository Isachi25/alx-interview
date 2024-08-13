#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys

# Initialize a dictionary to store counts of each status code
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize the total file size and line counter
total_size = 0
counter = 0

def print_stats():
    """Function to print the accumulated statistics."""
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value > 0:
            print('{}: {}'.format(key, value))

try:
    for line in sys.stdin:
        line_list = line.split()

        # Ensure the line has the expected format
        if len(line_list) > 4:
            try:
                code = line_list[-2]
                size = int(line_list[-1])

                # Update the status code count if it's a valid code
                if code in cache:
                    cache[code] += 1

                # Update the total file size
                total_size += size
            except (ValueError, IndexError):
                continue  # Skip lines with invalid format
            counter += 1

        # Print statistics after every 10 lines
        if counter == 10:
            print_stats()
            counter = 0

except KeyboardInterrupt:
    # Handle Ctrl+C interruption
    print_stats()
    raise

finally:
    # Print statistics before exiting
    print_stats()

