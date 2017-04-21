#!/usr/bin/python

import sys
import os
import json
import transmissionrpc


class Transmitter:
    @classmethod
    def upload_magnet(self, magnet, client):
        return client.add_torrent(magnet)

    @classmethod
    def parse_config(self, file):
        with open(file) as config:
            return json.load(config)

        return False

    @classmethod
    def get_client(self, config):
        return transmissionrpc.Client(config['host'], config['port'], config['user'], config['password'])

    @classmethod
    def run(self, magnet = None):
        if magnet == None and len(sys.argv) > 1:
            magnet = sys.argv[1]

        config = self.parse_config(os.path.dirname(os.path.abspath(__file__)) + '/config.json')
        client = self.get_client(config)
        status = self.upload_magnet(magnet, client)

if __name__ == "__main__":
    transmitter = Transmitter()
    transmitter.run()
