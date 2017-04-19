#!/usr/bin/python

import sys
import json
import transmissionrpc


class Transmitter:
    #TODO: implement
    @classmethod
    def upload_magnet(self, magnet, client):
        return False

    #TODO: implement
    @classmethod
    def parse_config(self, file):
        return False

    @classmethod
    def get_client(self, config):
        return transmissionrpc.Client(config.host, config.port, config.user, config.password)

    @classmethod
    def run(self, magnet = None):
        if magnet == None and len(sys.argv) > 1:
            magnet = sys.argv[1]

        config = parse_config('../config.json')
        client = get_client(config)
        status = upload_magnet(magnet, config, client)

