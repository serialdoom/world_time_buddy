# -*- coding: utf-8 -*-

"""
time conversions from different timezones
"""

from datetime import datetime, timedelta
import os
from pytz import timezone
from tabulate import tabulate
from termcolor import colored
import yaml


def get_version():
    """ return version information """
    return '0.1.0'


def get_time(dest_tz, delta=0):
    """docstring for get_time"""
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    utc_time = datetime.now(timezone('UTC')) + timedelta(hours=delta)
    dest_time_now = utc_time.astimezone(timezone(dest_tz))

    time = dest_time_now.strftime(fmt).split(' ')
    return {
        'date': time[0],
        'time': ':'.join(time[1].split(':')[0:2]),
        'tz': time[2],
    }


def calc_range(cities):
    """Calculate how many hours to print

    Args:
        cities (list): a list of timezones to display
    Returns:
        The max number of hours to print as an int
    """
    dummy_rows, columns = os.popen('stty size', 'r').read().split()
    screen_characters = 0
    for city in cities:
        if len(city) > screen_characters:
            screen_characters = len(city)
    # | Europe/Belgium   |
    # | America/Los_Angeles |
    # ^^                   ^^  4 extra characters
    screen_characters += 4  # tabulate frames for timezone
    range_todo = 0
    while screen_characters < int(columns):
        # | HH:MM | HH:MM |
        # ------->        <--- this is 8
        screen_characters += 8
        range_todo += 1
    return range_todo


def main():
    """do main stuff"""

    import argparse
    parser = argparse.ArgumentParser(
        description='Calculate time in different timezones')
    # subparsers = parser.add_subparsers(help='commands')

    parser.add_argument('-r', '--hours',
                        type=int,
                        help='Calculated for range '
                        '-HOURS < now < HOURS. '
                        'If no range is provided, the script will '
                        'try to fill the terminal width with the '
                        'data')
    parser.add_argument('-t', '--timezone',
                        action='append',
                        default=[],
                        help='Timezone to display. Can be provided '
                        'multiple times')
    parser.add_argument('-c', '--config',
                        default='~/.wtb.yml',
                        help='Config file location')
    parser.add_argument('--no-color',
                        dest='color',
                        default=True,
                        action='store_false',
                        help='Disable color')
    parser.add_argument('-V', '--version',
                        action='version',
                        version='%(prog)s ' + get_version(),
                        help='Return the current version')

    args = parser.parse_args()
    config = None

    try:
        with open(os.path.expanduser(args.config)) as stream:
            config = yaml.load(stream)
        args.timezone += config['timezones']
    except IOError:
        print 'Error while loading config', args.config

    if args.hours is None:
        args.hours = calc_range(args.timezone)
    else:
        args.hours += 1

    hours = range(-args.hours/2+1, args.hours/2)
    results = []
    for city in args.timezone:
        result = [city]
        for i in hours:
            time = get_time(city, i)['time']
            if i == 0 and args.color:
                time = colored(time, 'white', attrs=['bold'])
            result.append(time)
        results += [result]
    print tabulate(results, headers=hours, tablefmt="fancy_grid")

if __name__ == '__main__':
    main()
