#!/usr/bin/python

import sys
import json
import transmissionrpc


def upload_magnet(magnet, client):
    #TODO: implement

def parse_config(file):
    #TODO: implement
    return False

def get_client(config):
    return transmissionrpc.Client(config.host, config.port, config.user, config.password)

def run(magnet = None):
    if magnet == None and len(sys.argv) > 1:
        magnet = sys.argv[1]

    config = parse_config('../config.json')
    client = get_client(config)
    status = upload_magnet(magnet, config, client)

