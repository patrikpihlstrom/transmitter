#!/usr/bin/python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from transmitter import transmitter


transmitter.Transmitter.run()

