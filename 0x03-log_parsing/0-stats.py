#!/usr/bin/python3
"""the `0-stats` module
reads logs from stdin and parses it to compute some metrics
"""
from datetime import datetime
from functools import reduce
import re
import sys


def date_valid(date):
    """checks if `date` is a valid date string"""
    try:
        datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S.%f")
        return True
    except ValueError:
        return False


def print_metrics(logs):
    """analyzes `logs` and prints the metrics"""
    # if logs is not empty
    if type(logs) is list and len(logs) > 0:
        file_sizes = list(map(lambda x: x[3], logs))
        valid_ip_logs = filter(lambda x: x[2] in [
                        200,
                        301,
                        400,
                        401,
                        403,
                        404,
                        405,
                        500,
                    ], logs)
        file_size = reduce(lambda x, y: x + y, file_sizes)
        all_status_codes = list(map(lambda x: x[2], valid_ip_logs))
        # gets the uniques status codes from list and sorts it
        # since set() only stores unique values
        unique_status_codes = list(set(all_status_codes))
        unique_status_codes.sort()

        print("File size: {}".format(file_size))
        for stat_code in unique_status_codes:
            print("{}: {}".format(
                stat_code,
                all_status_codes.count(stat_code))
            )
    else:
        print("File size: 0")


# if redirected from file or pipe
if not sys.stdin.isatty():
    try:
        logs = []
        for ln in sys.stdin:
            if all(char in ln for char in ["-", '"']):
                # parse the log into components
                ipadddress = ln[: ln.find("-")].strip()
                date = ln[ln.find("[") + 1: ln.find("]")].strip()
                header = ln[ln.find('"') + 1: ln.rfind('"')].strip()
                status_size = ln[ln.rfind('"') + 1:].strip().split(" ")

                # validate each component
                header_valid = header == "GET /projects/260 HTTP/1.1"
                size_valid = re.search(
                    r"102[0-4]|10[0-1][0-9]|[0-9]?[0-9]?[0-9]", status_size[1]
                )
                if status_size[0].isnumeric():
                    status_valid = True
                else:
                    status_size[0] = 0

                # if ip contains a single numeric characther
                # then check for pattern
                ip_valid = True
                if True in [char.isdigit() for char in ipadddress]:
                    ip_valid = re.search(
                        r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
                        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                        ipadddress,
                    )
                # if every section of the log is valid
                # store the log in the logs list
                if (
                    ip_valid and
                    date_valid(date) and
                    header_valid and
                    status_valid and
                    size_valid
                ):
                    temp = [
                        ipadddress,
                        date,
                        int(status_size[0]),
                        int(status_size[1])
                    ]
                    logs.append(temp)
                    if len(logs) % 10 == 0:
                        print_metrics(logs=logs)
        print_metrics(logs=logs)
    except KeyboardInterrupt:
        print_metrics()
