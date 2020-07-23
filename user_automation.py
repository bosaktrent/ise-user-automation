#!/usr/bin/env python3
"""
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import csv
import json

__author__ = "Trent Bosak <tbosak@cisco.com>"
__author__ = "Marwah Mahate <mmahate@cisco.com>"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

def main():
    # import from csv
    # creat needed json objects
    # json, uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types
    # send api request

    json_data = []

    with open('users.csv') as csv_data:
    	csv_reader = csv.DictReader(csv_data)
    	for csv_row in csv_reader:
    		json_data.append(csv_row)

    with open('users.json', 'w') as json_file:
    	json_file.write(json.dumps(json_data))

    return

if __name__ == '__main__':
    main()
