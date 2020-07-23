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

import requests
import urllib3
import pprint
import json
import csv
from crayons import blue, green, red

user_count = 0

def main():
    json_data = []

    print("Reading users from file...")

    with open('users.csv') as csv_data:
        csv_reader = csv.DictReader(csv_data)
        for csv_row in csv_reader:
            json_data.append(csv_row)

    for user in json_data:
        create_new_user(user)

    print("Added {} new users".format(user_count))

def create_new_user(user):
    url = "https://{}:{}/ers/config/internaluser".format(ip, port)
    dict = {
        "InternalUser" : {
            "id" : user['id'],
            "name" : user['name'],
            "description" : user['description'],
            "enabled" : user['enabled'],
            "email" : user['email'],
            "password" : user['password'],
            "firstName" : user['firstName'],
            "lastName" : user['lastName'],
            "changePassword" : user['changePassword'],
            "identityGroups": get_group_by_name(user['identityGroups']),
            "expiryDateEnabled" : user['expiryDateEnabled'],
            "expiryDate" : user['expiryDate'],
            "enablePassword" : user['enablePassword']
            }
        }
    payload = json.dumps(dict)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ==',
    }
    response = requests.request("POST", url, headers=headers, data = payload, verify=False)
    if response.status_code == 201:
        print(green(response.status_code) + " - added user: {} {}".format(user['firstName'], user['lastName']))
        global user_count
        user_count = user_count + 1
    else:
        print(red(response.status_code))

def get_group_by_name(name):
    url = "https://{}:{}/ers/config/identitygroup/name/{}".format(ip, port, name)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ==',
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()['IdentityGroup']['id']

if __name__ == '__main__':
    ip = "198.18.133.27" # ise ip address
    port = "9060" # port number for ise sdk
    urllib3.disable_warnings() # disable SSL warnings
    main()
