#!/usr/bin/python3
"""the `0-stats` module
reads logs from stdin and parses it to compute some metrics
"""
from datetime import datetime
from functools import reduce
import re
import sys