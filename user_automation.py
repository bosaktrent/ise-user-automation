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

__author__ = "Trent Bosak <tbosak@cisco.com>"
__author__ = "Marwah Mahate <mmahate@cisco.com>"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import requests
import urllib3
import pprint
import json

def main():
    # import from spreadsheet
    # creat needed json objects
    # send api request
    # get_all_identity_groups()
    # create_new_user()
    # get_group_by_name("Employee")
    # get_all_users()
    print_user_information()
    return

def get_all_identity_groups():
    url = "https://{}:{}/ers/config/identitygroup".format(ip, port)
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ==',
    }
    response = requests.request("GET", url, headers=headers, data = payload, verify=False)
    pprint.pprint(response.json())

def create_new_user():
    url = "https://{}:{}/ers/config/internaluser".format(ip, port)
    dict = {
        "InternalUser" : {
            "id" : "id",
            "name" : "test-trent",
            "description" : "description",
            "enabled" : True,
            "email" : "email@domain.com",
            "password" : "Pa55word1",
            "firstName" : "fName",
            "lastName" : "lName",
            "changePassword" : True,
            "identityGroups": "9efe2310-8c01-11e6-996c-525400b48521",
            "expiryDateEnabled" : False,
            "expiryDate" : "2020-12-11",
            "enablePassword" : "Pa55word1"
            }
        }
    payload = json.dumps(dict)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ==',
    }
    response = requests.request("POST", url, headers=headers, data = payload, verify=False)
    print(response.status_code)

def get_group_by_name(name):
    url = "https://{}:{}/ers/config/identitygroup/name/{}".format(ip, port, name)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ==',
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    pprint.pprint(response.json())

def get_all_users():
    url = "https://{}:{}/ers/config/internaluser".format(ip, port)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ=='
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    json_response = response.json()
    return json_response

def print_user_information():
    users = get_all_users()
    for user in users["SearchResult"]["resources"]:
        print("Name: {}, ID: {}".format(user["name"], user["id"]))

if __name__ == '__main__':
    ip = "198.18.133.27" # ise ip address
    port = "9060" # port number for ise sdk
    urllib3.disable_warnings() # disable SSL warnings
    main()
