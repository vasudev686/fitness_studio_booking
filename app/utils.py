from datetime import datetime
import pytz

def to_timezone(dt: datetime, timezone: str = "Asia/Kolkata") -> datetime:
    utc = pytz.utc.localize(dt)
    return utc.astimezone(pytz.timezone(timezone))
