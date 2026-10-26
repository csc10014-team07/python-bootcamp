"""Check thesis registration eligibility and report missing requirements."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether a student meets the thesis registration requirements."""
    return credits >= 120 and gpa >= 2


def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of unmet thesis registration requirements.

    Print a confirmation if the student meets all requirements.

    Args:
        credits: The student's completed credits.
        gpa: The student's current GPA.

    Returns:
        A list of messages describing unmet requirements.
    """
    mylist: list[str] = []

    if can_register_thesis(credits, gpa):
        print("Can register")
    else:
        if credits < 120:
            mylist.append("need " + str(120 - credits) + " more credits")
        if gpa < 2:
            mylist.append("need higher gpa by " + str(2 - gpa))

    return mylist


print(missing(118, 1.0))