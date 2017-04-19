#!/usr/bin/python

import sys
from os import path
import unittest
import json

sys.path.append(path.dirname(path.abspath(__file__))+'/../')
from transmitter import transmitter


class TestTransmitter(unittest.TestCase):
    def test_parse_config(self):
        config = transmitter.parse_config('./example_config.json')
        example_config = {"user": "user", "password": "password", "host": "host", "port": 123}
        self.assertEqual(config, example_config)

    def test_parse_config_not_found(self):
        self.assertFalse(transmitter.parse_config('./not_found.json'))

    def test_upload_magnet(self):
        config = transmitter.parse_config('./config.json')
        self.assertNotEqual(config, False)

        client = transmitter.get_client(transmitter.parse_config('./config'))
        torrents = client.get_torrents()
        client.add_torrent(config['magnet'])
        self.assertNotEqual(torrents, client.get_torrents())

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTransmitter('test_parse_config'))
    suite.addTest(TestTransmitter('test_parse_config_not_found'))
    suite.addTest(TestTransmitter('test_upload_magnet'))

    unittest.TextTestRunner().run(suite)

