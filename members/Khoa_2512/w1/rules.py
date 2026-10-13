def can_register_thesis(credits: int, gpa: float) -> bool:
    if credits>=120 and gpa >=2:
        return True
    else:
        return False
def missing(credits, gpa)->list[str]:
    mylist=list()
    if can_register_thesis(credits, gpa):
        print("Can register")
    else:
        if credits<120:
           mylist.append("need "+ str(120-credits)+ " more credits")
        if gpa<2:
            mylist.append("need higher gpa by "+ str(2-gpa))
    return mylist
print(missing(118, 1.0))
    