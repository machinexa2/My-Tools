from lib.ColoredObject import Color as Cobj
from os import getenv

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
}

try:
    Headers['X-Bug-Bounty'] = getenv('HACKERONE_ACCESS_TOKEN')
except Exception:
    pass

ColorObj = Cobj()
