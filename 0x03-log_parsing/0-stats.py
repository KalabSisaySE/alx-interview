#!/usr/bin/python3
"""reads logs from stdin and parses it to compute some metrics"""
from dateutil import parser
from functools import reduce
import re
import sys


