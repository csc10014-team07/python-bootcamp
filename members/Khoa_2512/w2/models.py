from dataclasses import dataclass
@dataclass
class date:
    day: int
    month: int
    year: int 
    def __post_init__(self):
        if self.day<1 or self.month>12 or self.month<1 or self.year<0:
            raise ValueError("must be valid date")
        match self.month:
            case 2:
                limit=28
                if self.year%4:
                    limit=29
                if self.day>limit:
                    raise ValueError("must be valid date")
            case 1,3,5,7,8,10,12:
                if self.day>31:
                    raise ValueError("must be valid date")
            case _:
                if self.day>30:
                    raise ValueError("must be valid date")
    def __gt__(self, other):
        if self.year>other.year: return True
        if self.year==other.year and self.month>other.month: return True
        if self.year==other.year and self.month==other.month and self.day>other.day: return True
        return False
@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date
    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")
    def days_left(self, today: date) -> int:
        itoday=date(today.day, today.month, today.year)
        today_val=today.day+today.month*100+today.year*10000
        deadline_val=self.deadline.day+self.deadline.month*100+self.deadline.year*10000
        diff=deadline_val-today_val
        if diff<=0:
            print("Deadline have passed")
            return 0
        else:
            print("ok")
            result=0
            while itoday < self.deadline:
                itoday.day += 1

                if itoday.month == 2:
                    limit = 29 if itoday.year % 4 == 0 else 28
                elif itoday.month in (4, 6, 9, 11):
                    limit = 30
                else:
                    limit = 31

                if itoday.day > limit:
                    itoday.day = 1
                    itoday.month += 1

                    if itoday.month > 12:
                        itoday.month = 1
                        itoday.year += 1

                result += 1
        return result
