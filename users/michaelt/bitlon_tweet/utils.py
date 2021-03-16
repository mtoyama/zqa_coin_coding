import datetime
import pytz
from dateutil.parser import parse

def parse_and_localize_utc(date_string):
    utc = pytz.UTC
    parsed = parse(date_string)
    if parsed.tzinfo is not None and parsed.tzinfo.utcoffset(parsed) is not None:
        return parsed
    else:
        return utc.localize(parsed)