#!/usr/bin/python

import sys
import json
import transmissionrpc


if len(sys.argv) > 1:
    tc = transmissionrpc.Client('***REMOVED***', port=***REMOVED***, user='***REMOVED***', password='***REMOVED***')
    tc.add_torrent(sys.argv[1])
