from datetime import date, timedelta

def parse_due(text: str, today: date) -> date:
    text = text.strip().lower()
    
    if text == "tomorrow":
        return today + timedelta(days=1)
    
    if text.startswith("in ") and text.endswith(" days"):
        try:
            parts = text.split()
            days = int(parts[1])
            return today + timedelta(days=days)
        except (ValueError, IndexError):
            raise ValueError(f"Định dạng thời gian không hợp lệ: {text}")
            
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass
        
    day_map = {
        "mon": 0, "monday": 0,
        "tue": 1, "tuesday": 1,
        "wed": 2, "wednesday": 2,
        "thu": 3, "thursday": 3,
        "fri": 4, "friday": 4,
        "sat": 5, "saturday": 5,
        "sun": 6, "sunday": 6
    }
    
    if text in day_map:
        target_weekday = day_map[text]
        current_weekday = today.weekday()
        days_ahead = (target_weekday - current_weekday) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)
        
    raise ValueError(f"Không nhận diện được định dạng ngày hạn: {text}")