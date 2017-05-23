#!/usr/bin/python

import sys
from os import path
import unittest
import json
import time

sys.path.append(path.dirname(path.abspath(__file__))+'/../')
from transmitter import transmitter


class TestTransmitter(unittest.TestCase):
    transmitter = None

    def __init__(self, function):
        super(TestTransmitter, self).__init__(function)
        self.transmitter = transmitter.Transmitter

    def setUp(self):
        # get current torrents
        pass

    def tearDown(self):
        # remove added test torrents
        pass

    def test_upload_magnet(self):
        config = self.transmitter.parse_config('./config.json')
        self.assertNotEqual(config, False)

        client = self.transmitter.get_client(self.transmitter.parse_config('./config.json'))
        torrents = client.get_torrents()
        upload = self.transmitter.upload_magnet(config['magnet'], client)
        print "waiting for the server..."
        #time.sleep(10)
        self.assertNotEqual(str(torrents), str(client.get_torrents()))
        self.assertTrue(upload)

    def test_watch_downloads_directory(self):
        # add .torrent files
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestTransmitter('test_upload_magnet'))

    unittest.TextTestRunner().run(suite)

