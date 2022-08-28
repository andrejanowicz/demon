#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" demon.py  - DEparture MONitor
    demon.py connects to VRR Abfahrtsmonitor service and prints the results
    in a way to mimic the look of EVAG Departure Monitors.
    Usage: ./demon.py [city] [station] [offset] --platform 1,2,3,n --rows n
    Arguments [city] and [station] are mandatory.
"""

__author__ = 'André Janowicz'
__email__ = 'andre.janowicz@rub.de'
__version__ = '0.1'
__copyright__ = '2015, André Janowicz'
__license__ = 'GPLv3'

import argparse
import sys
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description='Departure Monitor')
parser.add_argument('city', type=str,
                    help='''city name,
                    use quotes to mask spaces or use '+' ''')
parser.add_argument('station', type=str,
                    help='''station name,
                    use quotes to mask spaces or use '+' ''')
parser.add_argument('offset',  nargs='?', default=0, type=int,
                    help='offset in minutes, default is 0')
parser.add_argument('-p', '--platforms', type=str,
                    help='comma seperated list of platforms')
parser.add_argument('-r', '--rows', default=3, type=int,
                    help='number of rows to display, default is 3, max is 40')
parser.add_argument('-c', '--color', default='yellow', type=str,
                    help='textcolor, available colors are: '
                    'black, red, green, yellow, blue, purple cyan and white. '
                    'Default is yellow.')

args = parser.parse_args()


def format_str(s, length, front=True):

    if length - len(s) >= 2:
        s = s.replace('str.', 'straße')
    s = s[0:length]
    if front:
        s += (length - len(s)) * ' '
    else:
        s = (length - len(s)) * ' ' + s
    return s


def this_platform(platform, platforms):

    if platforms is None:
        return True
    return str(platform) in platforms.split(',')

# .replace('ö','%F6').replace('ä','%E4').replace('ü','%FC')


city = args.city.lower().replace(' ', '+')
station = args.station.lower().replace(' ', '+')
platforms = args.platforms
offset = args.offset
offsettime = datetime.now() + timedelta(minutes=offset)
rows = args.rows

result = False

# Colors
black = '\033[0;30m'
red = '\033[0;31m'
green = '\033[0;32m'
yellow = '\033[0;33m'
blue = '\033[0;34m'
purple = '\033[0;35m'
cyan = '\033[0;36m'
white = '\033[0;37m'
# High Intensity
IBlack = '\033[0;90m'
IRed = '\033[0;91m'
IGreen = '\033[0;92m'
IYellow = '\033[0;93m'
IBlue = '\033[0;94m'
IPurple = '\033[0;95m'
ICyan = '\033[0;96m'
IWhite = '\033[0;97m'
# Bold
BBlack = '\033[1;30m'
BRed = '\033[1;31m'
BGreen = '\033[1;32m'
BYellow = '\033[1;33m'
BBlue = '\033[1;34m'
BPurple = '\033[1;35m'
BCyan = '\033[1;36m'
BWhite = '\033[1;37m'

reset = '\033[0m'

foreground = yellow

URL = "http://efa.vrr.de/vrr/XSLT_DM_REQUEST"
payload = {
    'useProFootSearch': 0,
    'reset': 'neue+Anfrage',
    'typeInfo_dm': 'invalid',
    'type_dm': 'stop',
    'itdDateDay': offsettime.day,
    'itdDateMonth': offsettime.month,
    'itdDateYear': offsettime.year,
    'itdTimeHour': offsettime.hour,
    'itdTimeMinute': offsettime.minute,
    'sessionID': 0,
    'placeInfo_dm': 'invalid',
    'nameState_dm': 'empty',
    'help': 'Hilfe',
    'mode': 'direct',
    'requestID': 0,
    'language': 'de',
    'ptOptionsActive': 1,
    'deleteAssignedStops_dm': 1,
    'submitButton': 'anfordern',
    'placeState_dm': 'empty',
    'nameInfo_dm': 'invalid',
    'name_dm': station,
    'place_dm': city,
    'command': '',
    'useRealtime': 1,
    'outputFormat': 'XML'
}
try:
    r = requests.post(URL, data=payload)
except requests.exceptions.RequestException as e:
    print('Request to:', URL, 'failed. \nReason:', e)
    sys.exit(1)

if int(r.status_code) == 200:
    root = ET.fromstring(r.content)

    for child in root.iter('itdDeparture'):

        platform = child.get('platform')
        countdown = int(child.get('countdown')) + offset
        number = child.find('itdServingLine').get('number')
        number = number.replace('InterCity', '').lstrip()
        direction = child.find('itdServingLine').get('direction')
        direction = direction.replace(city.title(), '').lstrip()

        if rows and this_platform(platform, platforms):
            result = True
            rows -= 1

            print(foreground, format_str(number, 8),
                  format_str(direction, 22),
                  format_str(str(countdown), 3, False), 'min', reset)

    if not result:
        print('No departure(s) found.')
    sys.exit(0)
else:
    print('Server at', URL, 'does not like to handle our request. \n')
    print('Reason: ', r.reason)
    sys.exit(1)
