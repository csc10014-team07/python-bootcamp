from .models import Task
from .io_utils import load_tasks

from .errors import InfeasiblePlan
from .errors import check_feasible

def main():
    try: 
        tasks=load_tasks("members/Khoa_2512/w2/test.csv")
    except:
        return ValueError("Failed to load file")
    for n in tasks:
        print (n.title, n.importance, n.effort_h, n.deadline.year,"-",n.deadline.month,"-", n.deadline.day)

if __name__ == "__main__":
    main()