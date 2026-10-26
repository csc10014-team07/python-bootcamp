from datetime import date, timedelta
import re
days={
    "mon": 1, "tue": 2, "wed": 3, "thu": 4, "fri": 5, "sat": 6, "sun": 7, 
}

def parse_due(text: str, today: date) -> date:
    data=text.strip().lower()
    if data=="tomorrow":
        return today + timedelta(1)
    found=re.match(r"^in\s+(\d+)\s+days?$", data)
    if found:
        delta=int(found.group(1))
        return today+timedelta(delta)
    if data in days:
        result=days[data]
        if result-today.weekday()-1<=0:
            return today+timedelta(result-today.weekday()+6)
        return today+timedelta(result-today.weekday()-1)
    try:
        return date.fromisoformat(data)
    except:
        raise ValueError("Format not recognized.")